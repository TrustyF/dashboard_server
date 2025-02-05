from flask import Blueprint
import subprocess

bp = Blueprint('vitals', __name__)


@bp.route("/get", methods=["GET"])
def get():
    format_temp = {'temp': 0, 'power': 0}

    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = round(int(f.read()) / 1000)  # Convert from milli degrees to Celsius
        format_temp['temp'] = temp

        output = subprocess.check_output(["vcgencmd", "measure_volts", "core"]).decode("utf-8")
        power = float(output.replace("volt=", "").replace("V\n", ""))
        format_temp['power'] = round(power * 10) / 10

    except Exception as e:
        pass

    return format_temp
