from flask import Flask
from flask import render_template
from cafes import good_locations
from flask import request

from os import environ

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = []
    return render_template('index.html', data=data, quiet=50, api_key=environ["APIKEY"])


@app.route('/location', methods=['GET', 'POST'])
def location():
    coords = request.args.get('location').split(",")
    lat = float(coords[0])
    lon = float(coords[1])
    quiet = int(request.args.get('quiet'))
    data = good_locations(lat, lon, quiet, 0)
    return render_template('index.html', data=data, quiet=quiet, api_key=environ["APIKEY"])


if __name__ == '__main__':
    app.run()
