import os
import time
from flask import Flask

import pyroscope_io as pyroscope

pyroscope.configure(
	app_name       = "ride-sharing-app",
	server_address = "http://pyroscope:4040",
	tags           = {
    "hostname": f'{os.getenv("HOSTNAME")}',
    "region":   f'{os.getenv("REGION")}',
	}
)

app = Flask(__name__)

def work(n):
    i = 0
    start_time = time.time()
    while time.time() - start_time < n:
        i += 1


@app.route("/bike")
def bike():
    pyroscope.tag({ "vehicle": "bike" })
    work(0.2)
    pyroscope.remove_tags("vehicle")
    return "<p>Bike ordered</p>"


@app.route("/scooter")
def scooter():
    pyroscope.tag({ "vehicle": "scooter" })
    work(0.3)
    pyroscope.remove_tags("vehicle")
    return "<p>Scooter ordered</p>"


@app.route("/car")
def car():
    pyroscope.tag({ "vehicle": "car" })
    work(0.4)
    pyroscope.remove_tags("vehicle")
    return "<p>Car ordered</p>"


@app.route("/")
def environment():
    result = "<h1>environment vars:</h1>"
    for key, value in os.environ.items():
        result +=f"<p>{key}={value}</p>"
    return result

if __name__ == '__main__':
    app.run(threaded=False, processes=1, host='0.0.0.0', debug=False)

