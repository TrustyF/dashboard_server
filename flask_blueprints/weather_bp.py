from app import cache
from flask import Blueprint
import requests

bp = Blueprint('weather', __name__)


@bp.route("/get", methods=["GET"])
@cache.cached(timeout=1800)
def get():
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast?latitude=49.2497&longitude=-123.1193&timezone=auto&forecast_days=1'
        '&current=temperature_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,cloud_cover'
        '&hourly=temperature_2m,apparent_temperature,precipitation_probability'
        '&daily=weather_code,temperature_2m_max,temperature_2m_min,uv_index_max').json()

    formatted = {
        'current': response.get('current'),
        'hourly': response.get('hourly'),
        'daily': response.get('daily'),
    }

    print(formatted)

    return formatted, 200
