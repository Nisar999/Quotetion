# 💥 Common Failure Demos — Quotetion

These intentional failure examples are used during the **Day 12 session** to teach students how to debug real-world deployment issues.

---

## How to Use These Demos

1. Show the working app first (✅ green badge on `main`)
2. Introduce each failure one at a time
3. Let students **guess the cause** before revealing it
4. Walk through the fix together
5. Use the `broken-demo` branch for the live YAML failure demo

---

## Failure 1: YAML Syntax Error (broken-demo Branch)

### 🔴 The Error

```
Error: .github/workflows/ci.yml
  (Line 25): mapping values are not allowed here
```

### 📄 The Broken YAML

```yaml
# ❌ BROKEN — incorrect indentation
jobs:
  backend-test:
    name: 🧪 Backend Tests
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout code
      uses: actions/checkout@v4    # ← WRONG: 'uses' should be indented under the '-'
```

### ✅ The Fix

```yaml
# ✅ FIXED — correct indentation
jobs:
  backend-test:
    name: 🧪 Backend Tests
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4  # ← CORRECT: indented under '-'
```

### 🔍 Root Cause

YAML is **indentation-sensitive**. The `uses:` key must be at the same level as `name:` inside the step. A single space difference can break the entire workflow.

### 🎓 Teaching Point

> "YAML is like Python — indentation matters. One wrong space and everything breaks."

### 🔧 How to Debug

1. Go to GitHub → Actions tab → click the failed run
2. Read the error message — it usually tells you the exact line number
3. Look for indentation issues at that line
4. Use a YAML linter: [yamllint.com](https://www.yamllint.com/)

### 📌 Live Demo: broken-demo Branch

```bash
# Create the broken branch
git checkout -b broken-demo
# Edit .github/workflows/ci.yml — remove indentation on 'uses:' line
git add .
git commit -m "broken: intentional YAML indentation error"
git push origin broken-demo

# Watch it fail in GitHub Actions!
# Then fix it:
git checkout main
```

---

## Failure 2: Missing Dependency

### 🔴 The Error

```
ModuleNotFoundError: No module named 'fastapi'
```

### 📄 What Went Wrong

Someone forgot to add `fastapi` to `requirements.txt`, or the CI workflow installs from the wrong file.

```yaml
# ❌ Wrong path
- name: Install dependencies
  run: pip install -r requirements.txt  # ← This looks in root, not backend/
```

### ✅ The Fix

```yaml
# ✅ Correct path
- name: Install dependencies
  run: pip install -r backend/requirements.txt
```

### 🔍 Root Cause

The CI runner starts in the **repository root**, not inside `backend/`. File paths must be relative to where the runner is.

### 🎓 Teaching Point

> "CI runners don't know your project structure. You must tell them exactly where everything is."

### 🔧 How to Debug

1. Check the CI logs — the error shows which module is missing
2. Verify the `requirements.txt` file contains the module
3. Verify the path in the workflow file is correct
4. Run `pip install -r backend/requirements.txt` locally to confirm

---

## Failure 3: Missing GitHub Secret

### 🔴 The Error

```
Warning: MOTIVATION_API_KEY not set — running without API key protection
```

(This is a **warning**, not a failure — the app still works!)

### 📄 What Went Wrong

The `MOTIVATION_API_KEY` secret was not configured in GitHub Settings → Secrets.

### ✅ The Fix

1. Go to GitHub → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `MOTIVATION_API_KEY`
4. Value: `quotetion-demo-key-2024`
5. Click "Add secret"

### 🔍 Root Cause

GitHub Secrets are **per-repository**. They don't transfer when you fork or clone a repo. Each developer must configure their own secrets.

### 🎓 Teaching Point

> "Secrets are like passwords — they're stored in a vault, not in your code. If you forget to put them in the vault, the code can't find them."

### 🔧 How to Debug

1. Check application logs for warning messages about missing keys
2. Go to Settings → Secrets → verify the secret name matches exactly (case-sensitive!)
3. Re-run the workflow after adding the secret

---

## Failure 4: Failed GitHub Action — Test Failure

### 🔴 The Error

```
FAILED backend/test_main.py::test_health - AssertionError: assert 500 == 200
```

### 📄 What Went Wrong

A code change broke the `/health` endpoint — maybe someone accidentally deleted the route or introduced a syntax error.

```python
# ❌ Typo breaks the endpoint
@app.get("/heatlh")  # ← Typo: "heatlh" instead of "health"
def health_check():
    return HealthResponse(status="ok")
```

### ✅ The Fix

```python
# ✅ Correct spelling
@app.get("/health")
def health_check():
    return HealthResponse(status="ok")
```

### 🔍 Root Cause

CI caught a bug that manual testing might miss. The test expected `/health` but the endpoint was misspelled.

### 🎓 Teaching Point

> "This is EXACTLY why we have CI/CD. The automated tests caught a typo before it reached production!"

### 🔧 How to Debug

1. Read the test failure message — it tells you which test failed and why
2. Compare the expected vs actual response
3. Check the code that the test is testing
4. Fix the code and push again

---

## Failure 5: Broken Deployment — Wrong Dockerfile Path

### 🔴 The Error (Render)

```
==> Build failed
Error: Dockerfile not found at ./Dockerfile
```

### 📄 What Went Wrong

The `render.yaml` points to the wrong Dockerfile path.

```yaml
# ❌ Wrong path
dockerfilePath: ./Dockerfile          # ← Looks in root (doesn't exist)
```

### ✅ The Fix

```yaml
# ✅ Correct path
dockerfilePath: ./backend/Dockerfile  # ← Points to backend directory
```

### 🔍 Root Cause

Render uses the `dockerfilePath` in `render.yaml` to find the Dockerfile. If the path is wrong, the build fails before any code runs.

### 🎓 Teaching Point

> "Deployment platforms read YOUR configuration files. If you give them the wrong directions, they get lost — just like GPS with wrong coordinates."

### 🔧 How to Debug

1. Read the Render deployment logs
2. Check the `render.yaml` file paths
3. Verify the Dockerfile exists at the specified path
4. Check `dockerContext` matches the directory containing your app code

---

## Failure 6: Wrong Backend URL

### 🔴 The Error (Streamlit Frontend)

```
🔌 Cannot connect to the backend. Make sure the FastAPI server is running.
```

### 📄 What Went Wrong

The frontend is trying to connect to the wrong backend URL.

```env
# ❌ Wrong URL (default localhost won't work on Hugging Face Spaces)
BACKEND_URL=http://localhost:8000
```

### ✅ The Fix

```env
# ✅ Correct URL (use the Render public URL)
BACKEND_URL=https://quotetion-backend.onrender.com
```

### 🔍 Root Cause

When the frontend is deployed to Hugging Face Spaces, `localhost:8000` refers to the HF Space's own machine — not your Render backend. You need the **public URL** of your Render service.

### 🎓 Teaching Point

> "localhost means 'this computer'. When your frontend and backend are on different computers (different cloud platforms), they need public addresses to find each other — just like you can't call your friend using your own phone number."

### 🔧 How to Debug

1. Open browser DevTools → Network tab → look for failed API requests
2. Check what URL the frontend is trying to reach
3. Verify the `BACKEND_URL` environment variable is set correctly in HF Spaces Settings
4. Test the backend URL directly in the browser: `https://your-backend.onrender.com/health`

---

## 📋 Quick Reference: Failure → Fix

| # | Failure | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | YAML Syntax Error | Wrong indentation | Fix indentation in ci.yml |
| 2 | Missing Dependency | Wrong file path in CI | Use `backend/requirements.txt` |
| 3 | Missing Secret | Secret not configured | Add secret in GitHub Settings |
| 4 | Test Failure | Code typo/bug | Fix the code, push again |
| 5 | Broken Deployment | Wrong Dockerfile path | Fix path in render.yaml |
| 6 | Wrong Backend URL | localhost in production | Use Render public URL |

---

## 🎯 Student Exercise

After showing these failures, challenge students to:

1. Identify which failure type they're seeing from the error message alone
2. Explain the root cause in their own words
3. Propose a fix before you show them the answer

> **Pro tip:** Let students debug in pairs. One reads the error, the other searches for the fix.
