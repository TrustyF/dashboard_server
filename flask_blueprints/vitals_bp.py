from flask import Blueprint
from app import cache
import subprocess

bp = Blueprint('vitals', __name__)

old_temp = 0


@bp.route("/get", methods=["GET"])
@cache.cached(timeout=300)
def get():
    global old_temp

    format_temp = {
        'temp': 0,
        'prev_temp': old_temp,
    }

    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
        temp_num = float(temp.replace("temp=", "").replace("'C\n", ""))
        old_temp = temp_num
        format_temp['temp'] = temp_num

    except Exception as e:
        print('vitals exception', e)

    return format_temp, 200
