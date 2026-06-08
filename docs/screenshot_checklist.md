# 📸 Screenshot Checklist — Quotetion

Use these screenshots for **NotebookLM**, **presentation slides**, and the **Day 12 session**.

---

## How to Use This Checklist

1. ✅ Take each screenshot after deployment is complete
2. ✅ Name files consistently: `01_github_repo.png`, `02_folder_structure.png`, etc.
3. ✅ Import into NotebookLM as visual sources
4. ✅ Use in slides to walk students through the deployment pipeline

---

## Screenshots (20 Total)

### 1. 🏠 GitHub Repository Home

| Detail | Description |
|--------|-------------|
| **What to capture** | GitHub repo page showing file list, README preview, green "Code" button, branch indicator showing `main` |
| **Why it matters** | Students see what a real GitHub project looks like — files, README, and repo metadata |
| **Concept taught** | **GitHub** — remote repository, version control, project hosting |

---

### 2. 📁 Project Folder Structure

| Detail | Description |
|--------|-------------|
| **What to capture** | VS Code or terminal showing the full folder tree: `backend/`, `frontend/`, `docs/`, `.github/`, Docker files |
| **Why it matters** | Shows clean, organized architecture — students understand how real projects are structured |
| **Concept taught** | **Project Architecture** — separation of concerns, frontend/backend split |

---

### 3. ⚡ GitHub Actions Tab

| Detail | Description |
|--------|-------------|
| **What to capture** | GitHub → Actions tab showing workflow list with status icons (✅ and ❌) |
| **Why it matters** | Students see where CI/CD results appear — the "dashboard" for automated workflows |
| **Concept taught** | **CI/CD** — automated testing pipeline, workflow status monitoring |

---

### 4. ✅ Successful Workflow Run (main branch)

| Detail | Description |
|--------|-------------|
| **What to capture** | Expanded successful run showing all 3 green jobs: `🧪 Backend Tests`, `🎨 Frontend Verify`, `🐳 Build Verify` |
| **Why it matters** | Shows what a passing pipeline looks like — the "gold standard" for CI/CD |
| **Concept taught** | **CI/CD Success** — all checks passed, code is safe to deploy |

---

### 5. ❌ Failed Workflow Run (broken-demo branch)

| Detail | Description |
|--------|-------------|
| **What to capture** | Failed workflow run on `broken-demo` branch, showing red X, error message about YAML syntax |
| **Why it matters** | Students see what failure looks like and learn to read error messages |
| **Concept taught** | **Build Failure Debugging** — reading CI logs, understanding error messages |

---

### 6. ✅ Working Branch (main)

| Detail | Description |
|--------|-------------|
| **What to capture** | GitHub branch view showing `main` with green checkmark badge next to latest commit |
| **Why it matters** | Demonstrates the concept of a "healthy" branch with passing CI |
| **Concept taught** | **Branch Management** — main branch protection, CI status badges |

---

### 7. ❌ Broken Branch (broken-demo)

| Detail | Description |
|--------|-------------|
| **What to capture** | GitHub branch view showing `broken-demo` with red X badge, failed commit message |
| **Why it matters** | Contrast with the working branch — students see the visual difference between passing and failing |
| **Concept taught** | **Intentional Failure** — how to use branches for testing, debugging workflows |

---

### 8. 🔐 GitHub Secrets Page

| Detail | Description |
|--------|-------------|
| **What to capture** | Settings → Secrets and variables → Actions page showing `MOTIVATION_API_KEY` listed (value hidden with ***) |
| **Why it matters** | Students see how secrets are stored — values are NEVER visible once saved |
| **Concept taught** | **GitHub Secrets** — secure storage, environment variables, never hardcode secrets |

---

### 9. 📄 Workflow YAML File

| Detail | Description |
|--------|-------------|
| **What to capture** | `.github/workflows/ci.yml` open in GitHub's code viewer with syntax highlighting |
| **Why it matters** | Students read the actual workflow file and connect YAML syntax to GitHub Actions concepts |
| **Concept taught** | **GitHub Actions Syntax** — triggers, jobs, steps, environment variables |

---

### 10. 📖 FastAPI Swagger Docs

| Detail | Description |
|--------|-------------|
| **What to capture** | Browser showing `http://localhost:8000/docs` — Swagger UI with all 3 endpoints expanded, showing request/response schemas |
| **Why it matters** | Students see auto-generated API documentation — a professional practice |
| **Concept taught** | **API Documentation** — Swagger/OpenAPI, self-documenting APIs, request/response schemas |

---

### 11. 🌐 Render Dashboard

| Detail | Description |
|--------|-------------|
| **What to capture** | Render dashboard showing `quotetion-backend` service with status "Live" (green) |
| **Why it matters** | Students see a real cloud deployment dashboard — their code running on the internet |
| **Concept taught** | **Cloud Deployment** — Render platform, web services, deployment status |

---

### 12. 📋 Render Deployment Logs

| Detail | Description |
|--------|-------------|
| **What to capture** | Render → Events/Logs tab showing build logs (Docker build) and deploy logs (service starting) |
| **Why it matters** | Students learn to read deployment logs — critical for debugging production issues |
| **Concept taught** | **Deployment Debugging** — reading build logs, identifying failures, Docker build process |

---

### 13. 🔗 Render Public API URL

| Detail | Description |
|--------|-------------|
| **What to capture** | Browser showing the Render public URL + `/health` returning `{"status": "ok"}` as JSON |
| **Why it matters** | Proof that the backend is live and publicly accessible on the internet |
| **Concept taught** | **Public APIs** — health endpoints, API accessibility, base URLs |

---

### 14. 🤗 Hugging Face Space Dashboard

| Detail | Description |
|--------|-------------|
| **What to capture** | HF Spaces page showing the Quotetion space card with status "Running", SDK badge showing "Docker" |
| **Why it matters** | Students see another deployment platform — diversity in hosting options |
| **Concept taught** | **Hugging Face Spaces** — frontend hosting, alternative to Vercel/Netlify |

---

### 15. ⚙️ Hugging Face Space Settings

| Detail | Description |
|--------|-------------|
| **What to capture** | Space Settings → Repository secrets/Variables showing `BACKEND_URL` set to the Render public URL |
| **Why it matters** | Shows how frontend connects to backend across platforms using environment variables |
| **Concept taught** | **Environment Variables** — configuration management, cross-platform connectivity |

---

### 16. 🖥️ Live Streamlit Application

| Detail | Description |
|--------|-------------|
| **What to capture** | Full Streamlit app with results showing: category badge, motivation card, quote card, action step card — after entering "I am preparing for placements" |
| **Why it matters** | The final product — students see their deployed application working end-to-end |
| **Concept taught** | **Full-Stack Application** — frontend-backend communication, user experience |

---

### 17. 📊 Backend JSON Response

| Detail | Description |
|--------|-------------|
| **What to capture** | Browser or Postman showing raw JSON response from `/generate` with all 4 fields: `category`, `motivation`, `quote`, `action_step` |
| **Why it matters** | Students see the actual data format — JSON as the universal API language |
| **Concept taught** | **API Responses** — JSON format, structured data, API testing |

---

### 18. 🐳 Docker Containers Running

| Detail | Description |
|--------|-------------|
| **What to capture** | Terminal showing `docker ps` output with both containers: `quotetion-backend` and `quotetion-frontend` with their ports and status |
| **Why it matters** | Students see containers as running processes — not just config files |
| **Concept taught** | **Docker Containers** — container lifecycle, port mapping, container names |

---

### 19. 🔧 Docker Compose Output

| Detail | Description |
|--------|-------------|
| **What to capture** | Terminal showing `docker-compose up --build` output — both services building and starting with log output |
| **Why it matters** | Students see multi-container orchestration in action — one command to rule them all |
| **Concept taught** | **Docker Compose** — multi-container apps, service orchestration, build process |

---

### 20. 📘 FastAPI ReDoc

| Detail | Description |
|--------|-------------|
| **What to capture** | Browser showing `http://localhost:8000/redoc` — alternative API docs with clean layout |
| **Why it matters** | Shows that APIs can have multiple documentation styles — ReDoc vs Swagger UI |
| **Concept taught** | **API Documentation Styles** — different doc generators, developer experience |

---

## 📋 Quick Checklist

```
[ ] 01 — GitHub Repository Home
[ ] 02 — Project Folder Structure
[ ] 03 — GitHub Actions Tab
[ ] 04 — ✅ Successful Workflow Run (main)
[ ] 05 — ❌ Failed Workflow Run (broken-demo)
[ ] 06 — ✅ Working Branch (main)
[ ] 07 — ❌ Broken Branch (broken-demo)
[ ] 08 — GitHub Secrets Page
[ ] 09 — Workflow YAML File
[ ] 10 — FastAPI Swagger Docs
[ ] 11 — Render Dashboard
[ ] 12 — Render Deployment Logs
[ ] 13 — Render Public API URL
[ ] 14 — Hugging Face Space Dashboard
[ ] 15 — Hugging Face Space Settings
[ ] 16 — Live Streamlit Application
[ ] 17 — Backend JSON Response
[ ] 18 — Docker Containers Running
[ ] 19 — Docker Compose Output
[ ] 20 — FastAPI ReDoc
```
