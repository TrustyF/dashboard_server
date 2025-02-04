from flask import Blueprint
from app import cache
import subprocess

bp = Blueprint('vitals', __name__)


@bp.route("/get", methods=["GET"])
@cache.cached(timeout=300)
def get():
    format_temp = {'temp': 0}

    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
        format_temp['temp'] = float(temp.replace("temp=", "").replace("'C\n", "")), 200
    except Exception as e:
        print('vitals exception', e)

    return format_temp, 200
