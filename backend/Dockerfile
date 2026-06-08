# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Quotetion Backend — Dockerfile
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Uses python:3.11-slim for small image size (~150MB)
# Installs dependencies first (cached layer)
# Then copies application code
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Step 1: Use a lightweight Python image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements first (Docker caches this layer)
# If requirements don't change, Docker skips reinstalling
COPY requirements.txt .

# Step 4: Install Python dependencies
# --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application code
COPY . .

# Step 6: Tell Docker this container uses port 8000
EXPOSE 8000

# Step 7: Start the FastAPI server
# --host 0.0.0.0 makes it accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
