"""
Quotetion — Pydantic Models
============================
Defines request and response schemas for the API.
Used by FastAPI for automatic validation and Swagger docs.
"""

from pydantic import BaseModel, Field


class SituationRequest(BaseModel):
    """Request body for the /generate endpoint."""

    situation: str = Field(
        ...,
        min_length=2,
        max_length=500,
        description="Describe your current situation or challenge",
        examples=["I am preparing for placements"],
    )


class MotivationResponse(BaseModel):
    """Response body returned by /generate and /surprise endpoints."""

    category: str = Field(
        ...,
        description="The category of the motivation",
        examples=["Placements"],
    )
    motivation: str = Field(
        ...,
        description="A motivational message for the user",
        examples=["Keep going. Consistent effort always beats temporary fear."],
    )
    quote: str = Field(
        ...,
        description="An inspirational quote",
        examples=[
            "Success is the sum of small efforts repeated day in and day out."
        ],
    )
    action_step: str = Field(
        ...,
        description="A concrete recommended action step",
        examples=["Spend 30 minutes solving one aptitude problem today."],
    )


class HealthResponse(BaseModel):
    """Response body for the /health endpoint."""

    status: str = Field(
        default="ok",
        description="Health status of the API",
    )
