# ⚙️ DevOps Task Platform

<div align="center">

![DevOps Task Platform](https://img.shields.io/badge/DevOps-Task%20Platform-0d1117?style=for-the-badge&logo=gear&logoColor=4f8ef7)

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)
[![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/ec2/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/)

**A production-style full-stack task management platform built with real DevOps principles.**  
**Containerized · CI/CD Automated · Cloud Deployed · Version Controlled**

[🚀 Live Demo](#-live-deployment) · [📸 Screenshots](#-screenshots) · [⚙️ Setup](#-local-development-setup) · [🔄 CI/CD Pipeline](#-cicd-pipeline)

</div>

---

## 📌 Project Overview

**DevOps Task Platform** is a full-stack task management web application built to demonstrate a real-world DevOps workflow — from local containerization to automated cloud deployment via a GitHub Actions CI/CD pipeline.

**Skills demonstrated:**

- **Docker & Docker Compose** — 4-container multi-service orchestration
- **GitHub Actions** — automated build → push → deploy pipeline (~41 seconds end-to-end)
- **AWS EC2** — cloud deployment on Ubuntu LTS with production-style access controls
- **Docker Hub** — versioned image registry (v1 → v2 → v3)
- **SSH key authentication** — secure, passwordless automated deployment
- **Nginx** — reverse proxy routing frontend and backend through a single port
- **Portfolio UI** — professional dark-themed frontend built for portfolio credibility

---

## ✨ Features

### Application
- User registration and login with session management
- Full CRUD task management — add, update status, delete
- Task status cycling: Pending → In Progress → Completed
- Real-time stat cards (Total / Pending / In Progress / Completed)
- Filter tabs and inline success/error feedback

### Infrastructure & DevOps
- 4-container Docker Compose architecture (frontend, backend, mysql, nginx)
- Versioned Docker images pushed to Docker Hub
- GitHub Actions CI/CD pipeline triggered on every push to `main`
- AWS EC2 deployment with GitHub Secrets managing all credentials
- Full pipeline completes in **~41 seconds**

---

## 🏗️ Architecture

```
                        ┌─────────────────────────────────────┐
                        │          AWS EC2 Instance            │
                        │         Ubuntu LTS                   │
                        │                                      │
  User Browser ──HTTP──►│  ┌──────────────────────────────┐   │
                        │  │     Nginx Container (:80)     │   │
                        │  │    (Reverse Proxy / Router)   │   │
                        │  └────────┬──────────────────────┘   │
                        │           │                           │
                        │    ┌──────┴──────┐                   │
                        │    │             │                   │
                        │  ┌─▼──────┐  ┌──▼──────┐           │
                        │  │Frontend│  │ Backend │            │
                        │  │(Nginx) │  │ (Flask/ │            │
                        │  │ :80    │  │Gunicorn)│            │
                        │  │        │  │  :5000  │            │
                        │  └────────┘  └────┬────┘            │
                        │                   │                  │
                        │             ┌─────▼──────┐          │
                        │             │   MySQL 8  │          │
                        │             │   :3306    │          │
                        │             └────────────┘          │
                        └─────────────────────────────────────┘

  GitHub ──push──► GitHub Actions ──build/push──► Docker Hub
                          └──────────SSH──────────► EC2 Deploy
```

---

## 🔄 CI/CD Workflow

```
Developer pushes code
        │
        ▼
  GitHub Actions triggered (on: push → main)
        │
        ├─► Checkout source code
        ├─► Login to Docker Hub
        ├─► Build Backend Image   (8s)
        ├─► Build Frontend Image  (3s)
        ├─► Build Nginx Image     (1s)
        ├─► Push Backend Image    (8s)
        ├─► Push Frontend Image   (4s)
        ├─► Push Nginx Image      (4s)
        └─► Deploy to EC2 via SSH (1s)
                  │
                  ▼
          EC2: docker compose pull + up -d
                  │
                  ▼
        Live at http://<EC2-PUBLIC-IP>
```

**Total pipeline duration: ~41 seconds** ✅

---

## 🧰 Tech Stack

| Category | Technology | Purpose |
|---|---|---|
| **Frontend** | HTML, CSS, JavaScript | UI & interactivity |
| **Backend** | Python 3.11, Flask, Gunicorn | REST API server |
| **Database** | MySQL 8 | Persistent data storage |
| **Containerization** | Docker, Docker Compose | Multi-container orchestration |
| **Reverse Proxy** | Nginx (Alpine) | Routing & static file serving |
| **CI/CD** | GitHub Actions | Automated build & deploy pipeline |
| **Registry** | Docker Hub | Versioned image storage |
| **Cloud** | AWS EC2 (Ubuntu LTS) | Cloud hosting |
| **Auth** | SSH RSA 4096-bit keys | Secure EC2 access |
| **Secrets** | GitHub Repository Secrets | Credential management |

---

## 🏷️ GitHub Repository Topics

Add these topics to your repository (**Settings → Topics**) to improve discoverability:

`devops` `docker` `aws` `ec2` `github-actions` `cicd` `flask` `nginx` `mysql` `docker-compose` `python`

---

## 📁 Repository Structure

```
devops-task-platform/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD pipeline
│
├── backend/
│   ├── app.py                     # Flask application & API routes
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── Dockerfile
│
├── nginx/
│   ├── nginx.conf                 # Reverse proxy configuration
│   └── Dockerfile
│
├── screenshots/                   # Deployment proof screenshots
├── docker-compose.yml
├── .env.example                   # Environment variable template
├── .gitignore
└── README.md
```

---

## 💻 Local Development Setup

### Prerequisites

- Docker & Docker Compose
- Git

### Clone & Run

```bash
git clone https://github.com/au422621106016/devops-task-platform.git
cd devops-task-platform

cp .env.example .env
# Edit .env with your values

docker compose build --no-cache
docker compose up -d
```

Open **http://localhost** in your browser.

### Common Commands

```bash
docker compose down               # Stop all containers
docker compose logs -f backend    # Stream backend logs
docker compose build backend      # Rebuild a single service
docker ps                         # View running containers
```

---

## 🐳 Docker Compose

```yaml
services:

  frontend:
    image: jsdaya2211/frontend:v3
    container_name: frontend

  backend:
    image: jsdaya2211/backend:v3
    container_name: backend
    env_file:
      - .env
    depends_on:
      - mysql

  mysql:
    image: mysql:8
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: devopsdb
    volumes:
      - mysql-data:/var/lib/mysql

  nginx:
    image: jsdaya2211/nginx:v2
    container_name: nginx
    ports:
      - "80:80"
    depends_on:
      - frontend
      - backend

volumes:
  mysql-data:
```

All containers communicate on the `devops-task-platform_default` Docker network.

---

## 🔐 Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```env
MYSQL_ROOT_PASSWORD=
MYSQL_DATABASE=
FLASK_SECRET_KEY=
```

Never commit the `.env` file — it is listed in `.gitignore`.

---

## 🔒 Security

Never push sensitive files publicly. Ensure your `.gitignore` includes at minimum:

```
.env
*.pem
id_rsa
id_rsa.pub
.ssh/
```

The GitHub Actions pipeline handles all credentials exclusively through GitHub Repository Secrets — no secrets are ever written into code, logs, or committed files.

---

## ☁️ EC2 Deployment

**Instance configuration:**
- AMI: Ubuntu LTS
- Instance Type: t2.micro / t3.micro (verify your actual instance)
- Region: US East (N. Virginia)
- Security Group: HTTP (80), SSH (22)

**Deployment steps:**

```bash
# Connect to EC2
ssh -i /path/to/key.pem ubuntu@<EC2-PUBLIC-IP>

# Install Docker
sudo apt update && sudo apt install docker.io docker-compose-plugin -y
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Pull images and start containers
docker compose pull
docker compose up -d
```

---

## 🔑 SSH Authentication for CI/CD

GitHub Actions authenticates to EC2 using RSA 4096-bit SSH keys — no passwords involved.

```bash
# Generate key pair (local machine)
ssh-keygen -t rsa -b 4096 -C "github-actions"

# Add public key to EC2
echo "<public-key>" >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
```

The private key is stored as a GitHub Secret (`EC2_SSH_KEY`) and never exposed in code or logs.

---

## 🔒 GitHub Secrets

Navigate to **Settings → Secrets and Variables → Actions** and configure:

| Secret | Purpose |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub access token |
| `EC2_HOST` | EC2 public IP |
| `EC2_USER` | `ubuntu` |
| `EC2_SSH_KEY` | RSA private key contents |

---

## 🚀 CI/CD Pipeline

Defined in `.github/workflows/ci.yml`:

```yaml
name: Full CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      # -----------------------------------
      # Docker Hub Login
      # -----------------------------------
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      # -----------------------------------
      # Build Images
      # -----------------------------------
      - name: Build Backend Image
        run: |
          docker build -t jsdaya2211/backend:v3 ./backend

      - name: Build Frontend Image
        run: |
          docker build -t jsdaya2211/frontend:v3 ./frontend

      - name: Build Nginx Image
        run: |
          docker build -t jsdaya2211/nginx:v2 ./nginx

      # -----------------------------------
      # Push Images
      # -----------------------------------
      - name: Push Backend Image
        run: |
          docker push jsdaya2211/backend:v3

      - name: Push Frontend Image
        run: |
          docker push jsdaya2211/frontend:v3

      - name: Push Nginx Image
        run: |
          docker push jsdaya2211/nginx:v2

      # -----------------------------------
      # Deploy To EC2
      # -----------------------------------
      - name: Deploy to EC2
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ${{ secrets.EC2_USER }}
          key: ${{ secrets.EC2_SSH_KEY }}
          script: |
            cd devops-task-platform
            git fetch origin
            git reset --hard origin/main
            sudo docker compose down
            sudo docker compose pull
            sudo docker compose up -d
            sudo docker ps
```

| Step | Duration |
|---|---|
| Build (3 images) | ~12s |
| Push (3 images) | ~16s |
| Deploy via SSH | ~1s |
| **Total** | **~41s** |

---

## 🌐 Live Deployment

The application is deployed to **AWS EC2** — [Live Demo Coming Soon]

- ✅ Nginx reverse proxy on port 80
- ✅ Flask + Gunicorn backend API
- ✅ MySQL persistent storage
- ✅ Full task CRUD working end-to-end
- ✅ Deployed via automated GitHub Actions pipeline

---

## 📸 Screenshots

### 📊 Live Dashboard on EC2
> Dashboard running live on EC2 — task addition, status updates all functional

![Live Dashboard EC2](./screenshots/19-live-dashboard-ec2.png)

---

### ✅ GitHub Actions — Pipeline Success
> Workflow run complete — Status: **Success**, Duration: **41s**

![GitHub Actions Success](./screenshots/20-github-actions-success.png)

---

### 📋 GitHub Actions — Full Job Breakdown
> All steps green: Checkout → Login → Build (×3) → Push (×3) → Deploy to EC2

![GitHub Actions Job Detail](./screenshots/21-github-actions-job-detail.png)

---

### 🟢 All Containers Running
> MySQL, frontend, backend, nginx all up and healthy

![Docker Compose Up](./screenshots/02-docker-compose-up.png)

---

### 📋 Docker PS
> All 4 containers live: nginx (:80), backend (:5000), mysql (:3306), frontend (:80)

![Docker PS](./screenshots/03-docker-ps.png)

---

### 🔐 Live Login Page on EC2
> Professional dark login page served via Nginx on EC2 public IP

![Live Login EC2](./screenshots/18-live-login-ec2.png)

---

### ✅ EC2 Instance Running
> Instance Status: Running, us-east-1c

![EC2 Running](./screenshots/14-ec2-running.png)

---

### 🖥️ Local Docker Build
> Full 28/28 steps completed — `docker compose build --no-cache`

![Docker Compose Build](./screenshots/01-docker-compose-build.png)

---

### 🔵 Status Update in Action
> Tasks updated to IN PROGRESS — stat cards reflect changes in real time

![Dashboard In Progress](./screenshots/05-dashboard-in-progress.png)

---

### 🗂️ Docker Image Version History
> All versioned images (v1/v2/v3) alongside compose images and mysql:8

![Docker Images](./screenshots/08-docker-images.png)

---

### 📤 Docker Hub Push
> frontend:v3, backend:v3, nginx:v2 pushed — layers confirmed with digest SHAs

![Docker Push](./screenshots/09-docker-push.png)

---

### 🐳 Docker Hub Repositories
> All three repositories public and updated

![Docker Hub Repos](./screenshots/10-docker-hub-repos.png)

---

### 🔑 SSH Key Generation
> RSA 4096-bit key pair generated for GitHub Actions authentication

![SSH Keygen](./screenshots/12-ssh-keygen.png)

---

### 🔒 GitHub Repository Secrets
> 5 secrets configured: DOCKER_PASSWORD, DOCKER_USERNAME, EC2_HOST, EC2_SSH_KEY, EC2_USER

![GitHub Secrets](./screenshots/17-github-secrets.png)

---

## 🧗 Challenges & Engineering Decisions

**Docker Compose startup ordering** — MySQL readiness on container start required `depends_on` health checks and connection retry logic in Flask rather than a simple service dependency.

**Nginx reverse proxy routing** — Routing `/api/` to Flask while serving static files from the same port 80 required careful `location` block ordering to avoid path conflicts.

**SSH key formatting for GitHub Actions** — RSA private keys must preserve newlines exactly when stored as GitHub Secrets; `appleboy/ssh-action` is sensitive to key formatting, which required multiple iterations to get right.

**Docker group permissions on EC2** — The `ubuntu` user needed explicit `docker` group membership so GitHub Actions could run `docker compose` commands without `sudo`.

**Versioned image strategy** — Two parallel naming schemes (compose-named images for local dev, versioned images for Docker Hub) required consistent naming conventions in both `docker-compose.yml` and the CI pipeline.

---

## 🔮 Future Improvements

- [ ] HTTPS via Let's Encrypt + Certbot
- [ ] Docker health checks in Compose for reliable startup ordering
- [ ] Separate `docker-compose.prod.yml` and `docker-compose.dev.yml`
- [ ] Automated tests in CI before the build step
- [ ] **Terraform** — IaC for reproducible, version-controlled infrastructure provisioning
- [ ] **Ansible** — configuration management and automated EC2 setup
- [ ] **Kubernetes** — container orchestration for multi-replica deployments
- [ ] **Monitoring & Logging** — centralized observability with ELK stack or CloudWatch
- [ ] **Python automation scripts** — deployment helpers, health checks, and tooling
- [ ] **Cloud networking** — VPC, subnets, security groups, load balancers
- [ ] Slack/email notifications on pipeline success or failure

---

## 👨‍💻 Author

<div align="center">

**Jaya Prakash**

[![GitHub](https://img.shields.io/badge/GitHub-au422621106016-181717?style=for-the-badge&logo=github)](https://github.com/au422621106016)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-jsdaya2211-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/jsdaya2211)

*Building real DevOps skills through hands-on projects.*

</div>

---

<div align="center">

⭐ **If this project helped you, please give it a star!** ⭐

*Built with 🔧 Docker · ⚡ GitHub Actions · ☁️ AWS EC2 · 🐍 Python Flask*

</div>
