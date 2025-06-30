import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry


class OpenMeteo:
    def __init__(self):
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = retry_session)
        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(
            self,
            latitude,
            longitude,
            current: list[str] = ["precipitation", "cloud_cover"],
            forecast_days: int = 1
        ) -> pd.DataFrame:
    
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": current,
            "forecast_days": forecast_days
        }
        responses = self.openmeteo.weather_api(self.url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        return response