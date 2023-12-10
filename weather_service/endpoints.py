from typing import Annotated
from datetime import datetime
from random import uniform

from fastapi import APIRouter, Query

from .schemas import WeatherReportSchema


router = APIRouter()


@router.get(
    path='/weather',
    response_model=WeatherReportSchema,
)
# pylint: disable=unused-argument
async def get_weather(
        latitude: Annotated[float, Query(ge=-90., le=+90.)],
        longitude: Annotated[float, Query(ge=-180., le=+180.)],
        timestamp: Annotated[datetime, Query()],
):
    """
    Симуляция получения погоды в примечательном месте
    """
    return WeatherReportSchema(
        temperature=uniform(-50, +50),
        humidity=uniform(0, 100),
        wind_speed=uniform(0, 100),
        wind_direction=uniform(0, 360),
        air_pressure=uniform(400, 1000),
        timestamp=timestamp,
    )
