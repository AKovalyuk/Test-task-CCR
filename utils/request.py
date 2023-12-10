from datetime import datetime

from requests import get

from core.settings import WEATHER_PROVIDER


def get_weather(latitude: float, longitude: float, timestamp: datetime):
    return get(
        url=f'{WEATHER_PROVIDER}/weather',
        params={
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': timestamp.isoformat(),
        },
    ).json()
