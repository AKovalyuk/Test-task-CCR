from datetime import datetime

from core.celery import app
from utils import get_weather
from .models import Place, WeatherReport


@app.task(name='weather_task')
def weather_task():
    for place in Place.objects.all():
        now = datetime.now()
        result = get_weather(place.latitude, place.longitude, now)
        WeatherReport.objects.create(
            temperature=result['temperature'],
            humidity=result['humidity'],
            wind_speed=result['wind_speed'],
            wind_direction=result['wind_direction'],
            air_pressure=result['air_pressure'],
            place_id=place.id,
            timestamp=now,
        )
