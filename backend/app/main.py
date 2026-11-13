import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Load environment variables from .env if present
load_dotenv()

# Base directories
BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"
CITIES_FILE = DATA_DIR / "cities.json"

# Track server start time for uptime calculation
SERVER_START_TIME = time.time()

# FastAPI application initialization
app = FastAPI(
    title="PH Weather Advisory API",
    description=(
        "FastAPI backend for the Philippine Weather Advisory App. "
        "Provides weather health checks, city catalogs, and weather advisory services."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Enable CORS for frontend clients (e.g. React/Vite running locally)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic Schemas for API Documentation & Validation
class HealthResponse(BaseModel):
    status: str = Field(..., description="System health status", examples=["healthy"])
    timestamp: str = Field(
        ...,
        description="Current server timestamp in ISO 8601 UTC format",
        examples=["2026-11-14T00:00:00Z"],
    )
    uptime: int = Field(
        ..., description="Server running uptime in seconds", examples=[3600]
    )


class City(BaseModel):
    id: str = Field(..., description="Unique city slug identifier", examples=["manila"])
    name: str = Field(..., description="City display name", examples=["Manila"])
    province: Optional[str] = Field(None, description="Province name", examples=["NCR"])
    region: Optional[str] = Field(
        None, description="Administrative region", examples=["National Capital Region"]
    )
    postal_code: Optional[str] = Field(
        None, description="Postal zip code", examples=["1000"]
    )
    latitude: float = Field(..., description="Latitude coordinate", examples=[14.5995])
    longitude: float = Field(..., description="Longitude coordinate", examples=[120.9842])
    timezone: Optional[str] = Field(
        "Asia/Manila", description="IANA Timezone", examples=["Asia/Manila"]
    )


class CitiesResponse(BaseModel):
    cities: List[City] = Field(..., description="List of supported Philippine cities")


@app.get("/", tags=["General"])
def read_root():
    """
    API Root endpoint providing service information and helpful navigation links.
    """
    return {
        "message": "Welcome to the PH Weather Advisory API",
        "docs": "/docs",
        "health": "/health",
        "cities": "/cities",
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def get_health():
    """
    Health check endpoint returning service status, current UTC timestamp, and uptime in seconds.
    """
    uptime_seconds = int(time.time() - SERVER_START_TIME)
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "status": "healthy",
        "timestamp": now_utc,
        "uptime": uptime_seconds,
    }


@app.get("/cities", response_model=CitiesResponse, tags=["Cities"])
def get_cities():
    """
    Returns the list of Philippine cities loaded from MJ's cities.json.
    """
    if not CITIES_FILE.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Cities configuration file not found at: {CITIES_FILE}",
        )

    try:
        with open(CITIES_FILE, "r", encoding="utf-8") as file:
            cities_data = json.load(file)

        if not isinstance(cities_data, list):
            raise ValueError("cities.json format invalid: expected a JSON array")

        return {"cities": cities_data}
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error reading cities data: {str(exc)}",
        )


@app.get("/cities/{city_id}", response_model=City, tags=["Cities"])
def get_city_by_id(city_id: str):
    """
    Retrieve details for a specific city by its ID or slug (e.g. 'manila', 'cebu-city', 'davao-city').
    """
    if not CITIES_FILE.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Cities configuration file not found at: {CITIES_FILE}",
        )

    try:
        with open(CITIES_FILE, "r", encoding="utf-8") as file:
            cities_data = json.load(file)

        for city in cities_data:
            if (
                city.get("id") == city_id
                or city.get("name", "").lower() == city_id.lower()
            ):
                return city

        raise HTTPException(
            status_code=404,
            detail=f"City with id or name '{city_id}' was not found.",
        )
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error reading city data: {str(exc)}",
        )

