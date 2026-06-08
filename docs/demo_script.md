# 🎬 Demo Day Script — Quotetion

Complete demo script for the **Day 12 session** on Deployment, CI/CD, and DevOps.

**Duration:** ~60-75 minutes  
**Audience:** 2nd and 3rd year engineering students  
**Goal:** Walk students from local code → GitHub → CI/CD → live deployment

---

## 🎯 Demo Flow Overview

```
1. Introduction & Hook          (5 min)
2. Project Walkthrough          (10 min)
3. Local Demo                   (5 min)
4. GitHub & Version Control     (5 min)
5. GitHub Actions & CI/CD       (10 min)
6. GitHub Secrets               (5 min)
7. Docker & Docker Compose      (10 min)
8. Render Deployment            (5 min)
9. Hugging Face Spaces          (5 min)
10. Failure Debugging Demo      (10 min)
11. Q&A & Wrap Up               (5 min)
```

---

## 1. Introduction & Hook (5 min)

### Speaking Notes

> "Raise your hand if you've ever built a cool project on your laptop, showed it to a friend, and they said 'That's awesome! Can you send me the link?' — and you realized... there is no link. It only works on YOUR computer."

> "Today, we're going to fix that forever. By the end of this session, you'll know how to take ANY project and put it on the internet for the world to see."

### What to Show

- Open the **live Quotetion app** (Hugging Face Spaces URL)
- Type "I am preparing for placements" → click "Get Motivated"
- Show the result with the category badge
- Click "Surprise Me" a few times
- "This app is live. Anyone in the world can use it right now."

---

## 2. Project Walkthrough (10 min)

### Speaking Notes

> "Let's look under the hood. This project has two parts — a frontend that you see, and a backend that does the work."

### What to Show

1. **Open VS Code** with the project folder
2. Walk through the folder structure:

```
Quotetion/
├── backend/       ← "The brain — FastAPI API server"
│   ├── main.py    ← "The main app — 3 endpoints"
│   ├── data.py    ← "20+ motivational entries"
│   ├── models.py  ← "Data validation schemas"
│   └── Dockerfile ← "Recipe to containerize"
├── frontend/      ← "The face — Streamlit UI"
│   ├── app.py     ← "Everything you see on screen"
│   └── Dockerfile ← "Recipe to containerize"
├── .github/       ← "Automation — CI/CD"
│   └── workflows/
│       └── ci.yml ← "Robot that tests our code"
└── docker-compose.yml ← "Runs everything together"
```

3. **Open `backend/main.py`** → Show the 3 endpoints:
   - "GET /health — like a heartbeat monitor"
   - "POST /generate — the main brainpower"
   - "GET /surprise — random fun"

4. **Open `backend/data.py`** → Show 2-3 entries:
   - "No AI here! Just a curated list with keyword matching. Simple, fast, free."

5. **Open `frontend/app.py`** → Scroll through:
   - "Custom CSS for the glassmorphism look"
   - "API calls to the backend"
   - "Result cards with icons"

### Architecture Explanation

> "The frontend is like a waiter. It takes your order (situation), sends it to the kitchen (backend), and brings back your food (motivation). They communicate through HTTP — the same language your browser uses."

---

## 3. Local Demo (5 min)

### Speaking Notes

> "Let me run this on my machine first. Right now, only I can see it."

### Live Steps

```bash
# Terminal 1: Start backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# → Show http://localhost:8000/docs (Swagger!)
```

```bash
# Terminal 2: Start frontend
cd frontend
pip install -r requirements.txt
streamlit run app.py
# → Show http://localhost:8501
```

### What to Demonstrate

1. **Swagger Docs** at `/docs` → "FastAPI gives us free, beautiful API documentation!"
   - Expand `/generate` → click "Try it out" → enter situation → Execute
   - Show the JSON response with `category` field
2. **Streamlit app** → Test both buttons
3. **Key question to students:** "Who can access this right now?" → "Only me, because it's localhost"

---

## 4. GitHub & Version Control (5 min)

### Speaking Notes

> "Step 1 of deployment: put your code somewhere everyone can get it."

### What to Show

1. **GitHub repo** → Show the files, README preview
2. **Commit history** → "Every save is tracked"
3. **Branches** → Show `main` (working) and `broken-demo` (broken — we'll use this later!)

### Key Teaching Moment

> "Your code on GitHub is like your resume online. Recruiters WILL look at your GitHub. Clean code, good README, proper structure — it matters."

---

## 5. GitHub Actions & CI/CD (10 min)

### Speaking Notes

> "Now here's the magic. Every time we push code, a robot automatically tests it."

### What to Show

1. **Open `.github/workflows/ci.yml`** in GitHub
2. Walk through each section:
   - "The `on:` section is the trigger — like a motion sensor"
   - "The `jobs:` section lists what the robot does"
   - "Job 1: Run our pytest tests"
   - "Job 2: Verify the frontend has no syntax errors"
   - "Job 3: Build Docker images and test the health endpoint"
   - "Job 3 uses `needs:` — it waits for Jobs 1 & 2 to pass"

3. **Go to GitHub Actions tab** → Show a **successful run** on `main`:
   - Click into it → show all 3 green jobs
   - Click into "Backend Tests" → show pytest output
   - "All 8 tests passed. Our code is safe."

4. **Key question:** "What happens if a test fails?"
   - Show the `broken-demo` branch (we'll demo this in Section 10)

---

## 6. GitHub Secrets (5 min)

### Speaking Notes

> "Never. Put. Passwords. In. Code. Let me show you the right way."

### What to Show

1. **GitHub → Settings → Secrets** → Show `MOTIVATION_API_KEY`
   - "See how the value is hidden? Even I can't see it after saving."
2. **Open `backend/main.py`** → Show the API key handling:
   - "If the key is set → log 'configured'. If missing → log a warning. App still works either way."
3. **Open `ci.yml`** → Show `${{ secrets.MOTIVATION_API_KEY }}`:
   - "GitHub injects the secret at runtime. It never appears in logs."

### Key Teaching Moment

> "If you ever push a secret to GitHub, consider it compromised. Bots scan GitHub constantly for leaked API keys. They WILL find it within minutes."

---

## 7. Docker & Docker Compose (10 min)

### Speaking Notes

> "How many of you have heard 'it works on my machine'? Docker solves that problem forever."

### What to Show

1. **Open `backend/Dockerfile`** → Walk through each step:
   - "FROM python:3.11-slim — our starting point, like a blank OS"
   - "COPY requirements first — Docker caches this layer"
   - "EXPOSE 8000 — documentation, not a command"
   - "CMD — what runs when the container starts"

2. **Run Docker Compose:**

```bash
docker-compose up --build
```

3. **While it builds**, explain:
   - "Docker downloads the base image"
   - "Installs dependencies"
   - "Copies our code"
   - "Creates a container for each service"

4. **Show `docker ps`** → Two containers running
5. **Open the app** → "Same app, now running inside containers"

### Key Teaching Moment

> "The Dockerfile is like a recipe. The image is the prepared meal kit. The container is the meal being served. You can serve the same meal kit at any restaurant in the world — that's Docker's superpower."

---

## 8. Render Deployment (5 min)

### Speaking Notes

> "Now let's put the backend on the actual internet."

### What to Show

1. **Render Dashboard** → Show the `quotetion-backend` service
   - Status: "Live" (green)
2. **Deployment Logs** → Show build + deploy process
   - "Render reads our Dockerfile, builds the image, and runs it — exactly like we did locally"
3. **Public URL** → Open `https://quotetion-backend.onrender.com/health`
   - Show `{"status": "ok"}` in browser
   - "This API is now available to anyone, anywhere"
4. **Open `/docs`** → Show Swagger working on the live URL
5. **Show `render.yaml`** → "This file tells Render everything it needs to know"

---

## 9. Hugging Face Spaces (5 min)

### Speaking Notes

> "Backend is live. Now let's deploy the frontend."

### What to Show

1. **HF Spaces Dashboard** → Show the Space status
2. **Space Settings** → Show `BACKEND_URL` environment variable pointing to Render
   - "This is how the frontend knows where to send requests"
3. **Live App** → Open the public URL
   - Test "Get Motivated" → "This request just traveled from HF Spaces → Render → back to HF Spaces"
4. **Show the full pipeline:**
   - "Code → GitHub → CI passes → Deploy to Render (backend) + HF Spaces (frontend) → Public URL"

---

## 10. Failure Debugging Demo (10 min)

### Speaking Notes

> "Everything breaks. The skill isn't avoiding failures — it's knowing how to fix them. Let me show you."

### Live Demo: broken-demo Branch

1. **Show `main` branch** → All green ✅
2. **Switch to `broken-demo` branch in GitHub Actions** → Red ❌
3. **Click into the failed run** → Read the error:
   - "mapping values are not allowed here" at line X
4. **Ask students:** "What do you think went wrong?"
   - Let them guess
5. **Show the YAML diff** → Point out the indentation error
6. **Key lesson:** "One space. One single space broke the entire pipeline. YAML is unforgiving."

### Quick Fire Failures (Show screenshots/examples from `docs/failure_demos.md`)

| Show This | Ask Students |
|-----------|-------------|
| `ModuleNotFoundError: No module named 'fastapi'` | "Where would you look first?" |
| `Cannot connect to the backend` | "What's wrong with `http://localhost:8000` in production?" |
| `Dockerfile not found` | "What file should we check?" |

---

## 11. Q&A & Wrap Up (5 min)

### Speaking Notes

> "Today you learned the complete journey from code to deployment. Let me recap the pipeline."

### Show the Pipeline

```
📝 Write Code
    ↓
📦 Push to GitHub
    ↓
🤖 GitHub Actions runs tests
    ↓
✅ All tests pass
    ↓
☁️ Deploy backend to Render
    ↓
🤗 Deploy frontend to HF Spaces
    ↓
🌍 Public URL — anyone can use it!
```

### Closing Line

> "Every app you see on the internet — Instagram, Spotify, ChatGPT — went through this exact process. Code → Test → Deploy. Now you know how it works. Go build something and deploy it."

---

## 📋 Likely Student Questions & Answers

### General

| Question | Answer |
|----------|--------|
| "Is Render free?" | "Yes, the free tier is enough for learning. It sleeps after 15 min of inactivity and wakes up on the next request." |
| "Can I use Vercel instead of HF Spaces?" | "Yes! Vercel, Netlify, and Streamlit Cloud are all alternatives. We use HF Spaces because it supports Docker and Streamlit natively." |
| "Do I need Docker for deployment?" | "No, but it makes deployment consistent. Without Docker, you'd have to configure the server manually." |
| "How much does deployment cost?" | "For learning projects, everything we used today is free. Production apps may need paid plans for more resources." |

### Technical

| Question | Answer |
|----------|--------|
| "Why use FastAPI instead of Flask?" | "FastAPI has automatic docs (Swagger), type validation, and better performance. It's the modern choice." |
| "Can I use React instead of Streamlit?" | "Absolutely! Streamlit is simpler for teaching, but React would work great for a production frontend." |
| "What if my backend crashes on Render?" | "Render auto-restarts it. The health check endpoint helps Render monitor if the app is alive." |
| "How do I add a database?" | "Add a database service (like PostgreSQL) on Render and connect via environment variables. Same pattern we used for BACKEND_URL." |
| "Can two people deploy to the same Render service?" | "Yes, if they have access to the same GitHub repo. Render auto-deploys when the repo is updated." |

### Career/Practical

| Question | Answer |
|----------|--------|
| "Should I add deployment to my resume?" | "100% yes. 'Deployed and maintained a web application using Docker, GitHub Actions, and Render' is a strong resume bullet." |
| "Do companies use GitHub Actions?" | "Many do. Some use Jenkins, GitLab CI, or CircleCI instead, but the concepts are identical." |
| "What's Kubernetes?" | "It's Docker Compose on steroids — manages thousands of containers across multiple servers. You'll learn it later in your career." |

---

## 🎒 Pre-Demo Checklist

```
[ ] Backend running on Render (verify /health)
[ ] Frontend running on HF Spaces (verify it loads)
[ ] Both buttons work on the live app
[ ] GitHub Actions shows ✅ on main branch
[ ] GitHub Actions shows ❌ on broken-demo branch
[ ] GitHub Secrets page has MOTIVATION_API_KEY
[ ] Docker installed locally (docker --version)
[ ] docker-compose.yml works locally
[ ] Swagger docs accessible at /docs
[ ] All 8 backend tests pass
[ ] VS Code open with project folder
[ ] Two terminal windows ready
[ ] Presentation slides loaded
[ ] NotebookLM sources uploaded
[ ] Stable internet connection
[ ] Backup: screenshots in case of connectivity issues
```
