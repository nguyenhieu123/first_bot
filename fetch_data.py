import requests
import os

def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = os.getenv("HOROSCOPE_URL")
    params = {'sign': sign, 'day': day}
    response = requests.get(url, params)
    return response.json()
