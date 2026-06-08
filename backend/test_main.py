"""
Quotetion — Backend Tests
==========================
Tests for the FastAPI endpoints using pytest + httpx.
Run with: pytest test_main.py -v
"""

import pytest
from fastapi.testclient import TestClient
from main import app


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Create a test client
# This simulates HTTP requests without starting a real server
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
client = TestClient(app)


# ── Test 1: Health Check ──
def test_health():
    """Verify the /health endpoint returns status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


# ── Test 2: Generate Motivation ──
def test_generate():
    """Verify /generate returns all 4 fields including category."""
    response = client.post(
        "/generate",
        json={"situation": "I am preparing for placements"},
    )
    assert response.status_code == 200
    data = response.json()

    # Check all 4 required fields exist
    assert "category" in data
    assert "motivation" in data
    assert "quote" in data
    assert "action_step" in data

    # Check fields are non-empty strings
    assert len(data["category"]) > 0
    assert len(data["motivation"]) > 0
    assert len(data["quote"]) > 0
    assert len(data["action_step"]) > 0


# ── Test 3: Generate with Empty Input ──
def test_generate_empty():
    """Verify /generate rejects empty input with 422 validation error."""
    response = client.post(
        "/generate",
        json={"situation": ""},
    )
    # FastAPI returns 422 for validation errors
    assert response.status_code == 422


# ── Test 4: Surprise Me ──
def test_surprise():
    """Verify /surprise returns all 4 fields including category."""
    response = client.get("/surprise")
    assert response.status_code == 200
    data = response.json()

    # Check all 4 required fields exist
    assert "category" in data
    assert "motivation" in data
    assert "quote" in data
    assert "action_step" in data

    # Check fields are non-empty strings
    assert len(data["category"]) > 0
    assert len(data["motivation"]) > 0
    assert len(data["quote"]) > 0
    assert len(data["action_step"]) > 0


# ── Test 5: Generate with Short Input ──
def test_generate_too_short():
    """Verify /generate rejects single-character input."""
    response = client.post(
        "/generate",
        json={"situation": "x"},
    )
    assert response.status_code == 422


# ── Test 6: Generate with Unknown Topic ──
def test_generate_unknown_topic():
    """Verify /generate returns a fallback category for unrecognized input."""
    response = client.post(
        "/generate",
        json={"situation": "something completely random and unrelated"},
    )
    assert response.status_code == 200
    data = response.json()
    # Should fall back to "Motivation" category
    assert data["category"] == "Motivation"


# ── Test 7: Swagger Docs Available ──
def test_swagger_docs():
    """Verify Swagger UI is accessible at /docs."""
    response = client.get("/docs")
    assert response.status_code == 200


# ── Test 8: OpenAPI Schema Available ──
def test_openapi_schema():
    """Verify OpenAPI schema is accessible (used by Swagger)."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert data["info"]["title"] == "Quotetion API"
    assert data["info"]["version"] == "1.0.0"
