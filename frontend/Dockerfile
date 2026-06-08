# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Quotetion Frontend — Dockerfile
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Runs a Streamlit application
# Compatible with Hugging Face Spaces (Docker SDK)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Step 1: Use a lightweight Python image
FROM python:3.11-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy and install dependencies (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application code
COPY . .

# Step 5: Expose port 8501 (Streamlit default)
EXPOSE 8501

# Step 6: Start Streamlit
# --server.address=0.0.0.0  → accessible from outside container
# --server.port=8501         → default Streamlit port
# --server.headless=true     → no browser auto-open in container
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]
