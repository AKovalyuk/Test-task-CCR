from pydantic import BaseModel, Field


class WeatherReportSchema(BaseModel):
    temperature: float = Field(ge=-50., le=+50)
    humidity: float = Field(ge=0, le=100)
    wind_speed: float = Field(ge=0)
    wind_direction: float = Field(ge=0, le=360)
    air_pressure: float = Field(ge=400, le=1000)
