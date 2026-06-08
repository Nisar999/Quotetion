# 🌟 Quotetion

> **Tell us your challenge. We'll fuel your fire.**

A motivational quote generator built with **Streamlit** + **FastAPI** — designed for teaching **Deployment, CI/CD, Docker, and DevOps** concepts.

---

## ✨ What It Does

Users enter their current situation or challenge, and the app generates:

| Output | Example |
|--------|---------|
| 🏷️ **Category** | Placements |
| 💪 **Motivation** | Keep going. Consistent effort always beats temporary fear. |
| 💬 **Quote** | "Success is the sum of small efforts repeated day in and day out." |
| 🎯 **Action Step** | Spend 30 minutes solving one aptitude problem today. |

Also includes a **🎲 Surprise Me** button for random motivation!

---

## 🏗️ Architecture

```
┌──────────────────────────┐       HTTP        ┌──────────────────────────┐
│    Streamlit Frontend    │ ────────────────►  │     FastAPI Backend      │
│   (HF Spaces / :8501)   │  POST /generate    │    (Render / :8000)      │
│                          │  GET  /surprise    │                          │
│  • Situation Input       │  GET  /health      │  • Keyword Matching      │
│  • Category Badge        │ ◄──────────────── │  • Curated 20+ Dataset   │
│  • Motivation Card       │   JSON Response    │  • Input Validation      │
│  • Quote Card            │   {category,...}   │  • Swagger Docs          │
│  • Action Step Card      │                    │  • Optional API Key      │
└──────────────────────────┘                    └──────────────────────────┘
```

---

## 📁 Project Structure

```
Quotetion/
├── backend/
│   ├── main.py              # FastAPI app + Swagger metadata
│   ├── data.py              # Curated dataset with categories
│   ├── models.py            # Pydantic models
│   ├── test_main.py         # 8 pytest tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py               # Streamlit UI
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .streamlit/
│       └── config.toml      # Dark theme config
├── docs/
│   ├── screenshot_checklist.md
│   ├── failure_demos.md
│   ├── teaching_guide.md
│   └── demo_script.md
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions (3 jobs)
├── docker-compose.yml
├── render.yaml              # Render deployment config
├── .gitignore
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Nisar999/Quotetion.git
cd Quotetion
```

### 2. Set up environment variables

```bash
cp .env.example .env
# Edit .env if needed (everything works with defaults)
```

### 3. Start the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API is now running at **http://localhost:8000**
- Swagger Docs: **http://localhost:8000/docs**
- ReDoc: **http://localhost:8000/redoc**

### 4. Start the Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

The app is now running at **http://localhost:8501**

---

## 🐳 Docker

### Build and run both services

```bash
docker-compose up --build
```

### Stop containers

```bash
docker-compose down
```

### Access

| Service | URL |
|---------|-----|
| Frontend | http://localhost:8501 |
| Backend | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

---

## 🧪 Tests

```bash
cd backend
pip install -r requirements.txt
pytest test_main.py -v
```

---

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `POST` | `/generate` | Generate motivation from situation |
| `GET` | `/surprise` | Random motivation |
| `GET` | `/docs` | Swagger UI documentation |
| `GET` | `/redoc` | ReDoc documentation |

### Example Request

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"situation": "I am preparing for placements"}'
```

### Example Response

```json
{
  "category": "Placements",
  "motivation": "Keep going. Consistent effort always beats temporary fear.",
  "quote": "Success is the sum of small efforts repeated day in and day out. — Robert Collier",
  "action_step": "Spend 30 minutes solving one aptitude problem today."
}
```

---

## 🌐 Deployment

### Backend → Render

1. Push code to GitHub
2. Connect repo to [Render](https://render.com)
3. Use the `render.yaml` Blueprint
4. Set `MOTIVATION_API_KEY` in Environment (optional)
5. Deploy!

### Frontend → Hugging Face Spaces

1. Create a new Space → SDK: **Docker**
2. Upload the `frontend/` directory contents
3. Set `BACKEND_URL` to your Render URL in Space Settings → Variables
4. The Space will auto-build and deploy

---

## 🔐 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `MOTIVATION_API_KEY` | ❌ No | *(empty)* | Optional API key for teaching secrets |
| `BACKEND_URL` | ❌ No | `http://localhost:8000` | Backend URL for frontend |

---

## 🎓 Teaching Purpose

This project is designed for a **Day 12 session** covering:

- ✅ GitHub & Version Control
- ✅ GitHub Actions & CI/CD
- ✅ GitHub Secrets
- ✅ Docker & Docker Compose
- ✅ Render Deployment
- ✅ Hugging Face Spaces
- ✅ Build Failure Debugging

See the `docs/` folder for teaching guides, demo scripts, and failure examples.

---

## 📄 License

MIT
