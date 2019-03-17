from flask import Flask
from flask import render_template
from cafes import good_locations
from flask import request

from os import environ

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = good_locations(43.64469, -79.37996568810948, 0.5, 0.5)
    return render_template('index.html', data=data, api_key=environ["APIKEY"])


@app.route('/location', methods=['GET', 'POST'])
def location():
    coords = request.args.get('location').split(",")
    lat = float(coords[0])
    lon = float(coords[1])
    data = good_locations(lat, lon, 0.5, 0.5)
    return render_template('index.html', data=data, api_key=environ["APIKEY"])


if __name__ == '__main__':
    app.run()
