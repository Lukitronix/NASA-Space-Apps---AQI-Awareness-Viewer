# This file was made with the help of artificial intelligence.
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Location(BaseModel):
    lat: float
    lon: float

class AirQualityReading(BaseModel):
    timestamp: datetime
    pm25: Optional[float]
    pm10: Optional[float]
    no2: Optional[float]
    o3: Optional[float]
    co: Optional[float]

class LatestResponse(BaseModel):
    location: Location
    readings: List[AirQualityReading]
