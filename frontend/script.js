const API_URL = "/api";

let token = "";

// REGISTER USER
async function registerUser() {

    const username = document.getElementById("username").value;

    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/register`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username,
            password
        })
    });

    const data = await response.json();

    alert(data.message || data.error);
}


// LOGIN USER
async function loginUser() {

    const username = document.getElementById("username").value;

    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/login`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username,
            password
        })
    });

    const data = await response.json();

    if (data.token) {

        token = data.token;

        alert("Login Successful");

    } else {

        alert(data.message || "Login Failed");
    }
}


// ADD TASK
async function addTask() {

    const title = document.getElementById("taskInput").value;

    const response = await fetch(`${API_URL}/tasks`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },

        body: JSON.stringify({
            title
        })
    });

    const data = await response.json();

    alert(data.message || "Task Added");

    loadTasks();
}


// LOAD TASKS
async function loadTasks() {

    const response = await fetch(`${API_URL}/tasks`, {

        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const tasks = await response.json();

    console.log(tasks);

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    // Handle invalid response
    if (!Array.isArray(tasks)) {

        alert(tasks.message || tasks.msg || "Failed to load tasks");

        return;
    }

    tasks.forEach(task => {

        const li = document.createElement("li");

        li.innerHTML = `
            ${task.title} - ${task.status}
            <button onclick="deleteTask(${task.id})">
                Delete
            </button>
        `;

        taskList.appendChild(li);
    });
}


// DELETE TASK
async function deleteTask(id) {

    const response = await fetch(`${API_URL}/tasks/${id}`, {

        method: "DELETE",

        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await response.json();

    alert(data.message || "Task Deleted");

    loadTasks();
}