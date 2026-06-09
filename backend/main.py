"""
Quotetion — FastAPI Backend
============================
A simple motivational quote API for teaching deployment concepts.

Endpoints:
    GET  /health   → Health check
    POST /generate → Generate motivation based on user's situation
    GET  /surprise → Random motivation (no input needed)

Swagger Docs:
    GET  /docs     → Interactive API documentation
    GET  /redoc    → Alternative API documentation
"""

import os
import logging
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from models import SituationRequest, MotivationResponse, HealthResponse
from data import get_by_situation, get_random

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Load environment variables
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Logging setup
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("quotetion")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# API Key handling (OPTIONAL)
# App works without it — just logs a warning
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API_KEY = os.getenv("MOTIVATION_API_KEY")

if API_KEY:
    logger.info("✅ MOTIVATION_API_KEY is configured")
else:
    logger.warning(
        "⚠️  MOTIVATION_API_KEY not set — running without API key protection. "
        "This is fine for development and teaching purposes."
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Lifespan — runs on startup and shutdown
# (Modern replacement for @app.on_event)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Log startup and shutdown messages."""
    logger.info("🚀 Quotetion API is running!")
    logger.info("📖 Swagger docs available at /docs")
    logger.info("📘 ReDoc available at /redoc")
    yield
    logger.info("👋 Quotetion API shutting down")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FastAPI App with Swagger metadata
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
app = FastAPI(
    title="Quotetion API",
    description=(
        "🌟 **Quotetion** — A motivational quote generator API.\n\n"
        "Enter your current situation or challenge, and receive:\n"
        "- 💪 A motivational message\n"
        "- 💬 An inspirational quote\n"
        "- 🎯 A recommended action step\n"
        "- 🏷️ A category label\n\n"
        "Built for teaching **Deployment, CI/CD, Docker, and DevOps** concepts."
    ),
    version="1.0.0",
    contact={
        "name": "Quotetion Team",
    },
    license_info={
        "name": "MIT",
    },
    lifespan=lifespan,
    redoc_url=None,  # Disable default ReDoc (we serve a custom one below)
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Custom ReDoc route
# The default ReDoc CDN sometimes fails on free-tier hosting.
# This route uses a reliable CDN (cdn.redoc.ly) instead.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.get("/redoc", include_in_schema=False)
def custom_redoc():
    """Serve ReDoc with a reliable CDN."""
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Quotetion API — ReDoc</title>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
            <style>
                body { margin: 0; padding: 0; }
            </style>
        </head>
        <body>
            <redoc spec-url='/openapi.json'></redoc>
            <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
        </body>
        </html>
        """
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CORS Middleware
# Allow all origins for teaching simplicity
# In production, you would restrict this
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all origins (for teaching)
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


@app.get(
    "/",
    tags=["System"],
    summary="Welcome",
    description="Root endpoint — shows API info and available endpoints.",
)
def root():
    """Welcome endpoint with API overview."""
    return {
        "app": "Quotetion API",
        "version": "1.0.0",
        "message": "🌟 Welcome to Quotetion! A motivational quote generator API.",
        "endpoints": {
            "health": "/health",
            "generate": "/generate (POST)",
            "surprise": "/surprise",
            "docs": "/docs",
            "redoc": "/redoc",
        },
    }


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["System"],
    summary="Health Check",
    description="Returns the health status of the API. Used by Render and Docker for monitoring.",
)
def health_check():
    """Check if the API is running."""
    return HealthResponse(status="ok")


@app.post(
    "/generate",
    response_model=MotivationResponse,
    tags=["Motivation"],
    summary="Generate Motivation",
    description=(
        "Send your current situation or challenge, "
        "and receive a personalized motivation message, quote, and action step."
    ),
)
def generate_motivation(request: SituationRequest):
    """Generate motivation based on the user's situation."""
    logger.info(f"Generating motivation for situation: {request.situation[:50]}...")
    result = get_by_situation(request.situation)
    return MotivationResponse(**result)


@app.get(
    "/surprise",
    response_model=MotivationResponse,
    tags=["Motivation"],
    summary="Surprise Me",
    description="Get a random motivation message, quote, and action step — no input needed!",
)
def surprise_me():
    """Return a random motivation entry."""
    logger.info("Generating surprise motivation...")
    result = get_random()
    return MotivationResponse(**result)


