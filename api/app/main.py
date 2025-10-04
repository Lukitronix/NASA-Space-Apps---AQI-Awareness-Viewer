# This file was made with the help of artificial intelligence.
from fastapi import FastAPI, Query
from .data_cliente import get_latest_mock
from fastapi.middleware.cors import CORSMiddleware
from .models import LatestResponse


app = FastAPI(title="NASA Air Quality Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/air-quality/latest", response_model=LatestResponse)
async def air_quality_latest(lat: float = Query(...), lon: float = Query(...)):
    data = await get_latest_mock(lat, lon)
    return data

@app.get("/")
async def root():
    return {"message": "Backend de NASA Air Quality funcionando"}

