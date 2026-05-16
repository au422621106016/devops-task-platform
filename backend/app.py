from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from dotenv import load_dotenv

import mysql.connector
import os
import time


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()


# ==========================================
# FLASK APPLICATION SETUP
# ==========================================

app = Flask(__name__)

CORS(app)

app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY"
)

jwt = JWTManager(app)


# ==========================================
# MYSQL DATABASE CONNECTION
# ==========================================

connection = None

while connection is None:

    try:

        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )

        print("Connected to MySQL")

    except Exception as error:

        print("Waiting for MySQL...", error)

        time.sleep(5)


# ==========================================
# CREATE USERS TABLE
# ==========================================

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(255) UNIQUE,

    password VARCHAR(255)

)
""")


# ==========================================
# CREATE TASKS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (

    id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(255),

    status VARCHAR(50),

    user_id INT,

    FOREIGN KEY (user_id)
    REFERENCES users(id)

)
""")

connection.commit()

cursor.close()


# ==========================================
# HOME ROUTE
# ==========================================

@app.route("/")
def home():

    return jsonify({
        "message": "DevOps Task Platform API Running"
    })


# ==========================================
# USER REGISTRATION
# ==========================================

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")

    password = data.get("password")

    if not username or not password:

        return jsonify({
            "message": "Username and password required"
        }), 400

    if len(password) < 6:

        return jsonify({
            "message": "Password must be at least 6 characters"
        }), 400

    hashed_password = generate_password_hash(
        password
    )

    cursor = connection.cursor()

    try:

        cursor.execute(

            """
            INSERT INTO users
            (username, password)

            VALUES (%s, %s)
            """,

            (username, hashed_password)

        )

        connection.commit()

        return jsonify({
            "message": "User registered successfully"
        }), 201

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 400

    finally:

        cursor.close()


# ==========================================
# USER LOGIN
# ==========================================

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")

    password = data.get("password")

    if not username or not password:

        return jsonify({
            "message": "Username and password required"
        }), 400

    cursor = connection.cursor(dictionary=True)

    cursor.execute(

        """
        SELECT *
        FROM users
        WHERE username=%s
        """,

        (username,)

    )

    user = cursor.fetchone()

    cursor.close()

    if user and check_password_hash(
        user["password"],
        password
    ):

        access_token = create_access_token(
            identity=str(user["id"])
        )

        return jsonify({
            "token": access_token
        }), 200

    return jsonify({
        "message": "Invalid credentials"
    }), 401


# ==========================================
# GET TASKS
# ==========================================

@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():

    current_user = get_jwt_identity()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(

        """
        SELECT *
        FROM tasks
        WHERE user_id=%s
        """,

        (current_user,)

    )

    tasks = cursor.fetchall()

    cursor.close()

    return jsonify(tasks), 200


# ==========================================
# ADD TASK
# ==========================================

@app.route("/tasks", methods=["POST"])
@jwt_required()
def add_task():

    current_user = get_jwt_identity()

    data = request.get_json()

    title = data.get("title")

    if not title:

        return jsonify({
            "message": "Task title required"
        }), 400

    cursor = connection.cursor()

    cursor.execute(

        """
        INSERT INTO tasks
        (title, status, user_id)

        VALUES (%s, %s, %s)
        """,

        (title, "Pending", current_user)

    )

    connection.commit()

    cursor.close()

    return jsonify({
        "message": "Task added"
    }), 201


# ==========================================
# UPDATE TASK
# ==========================================

@app.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):

    current_user = get_jwt_identity()

    data = request.get_json()

    title = data.get("title")

    status = data.get("status")

    if not title or not status:

        return jsonify({
            "message": "Title and status required"
        }), 400

    cursor = connection.cursor()

    cursor.execute(

        """
        UPDATE tasks

        SET
            title=%s,
            status=%s

        WHERE
            id=%s
            AND user_id=%s
        """,

        (title, status, id, current_user)

    )

    connection.commit()

    cursor.close()

    return jsonify({
        "message": "Task updated"
    }), 200


# ==========================================
# DELETE TASK
# ==========================================

@app.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):

    current_user = get_jwt_identity()

    cursor = connection.cursor()

    cursor.execute(

        """
        DELETE FROM tasks
        WHERE
            id=%s
            AND user_id=%s
        """,

        (id, current_user)

    )

    connection.commit()

    cursor.close()

    return jsonify({
        "message": "Task deleted"
    }), 200


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )