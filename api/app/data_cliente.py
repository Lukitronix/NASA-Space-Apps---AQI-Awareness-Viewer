from datetime import datetime, timezone
from .models import AirQualityReading

async def get_latest_mock(lat: float, lon: float):
    now_utc = datetime.now(timezone.utc)
    reading = AirQualityReading(
        timestamp=now_utc,
        pm25=12.3,
        pm10=20.1,
        no2=5.2,
        o3=10.0,
        co=0.3
    )

    return {
        "location": {"lat": lat, "lon": lon},
        "readings": [reading]
    }