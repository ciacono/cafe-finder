from flask import Flask
from flask import render_template
from cafes import good_locations
from os import environ

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = good_locations(43.64469, -79.37996568810948, 0.5, 0.5)
    return render_template('index.html', data=data, api_key=environ["APIKEY"])


@app.route('/location')
def location(params):
    data = good_locations(params.lat, params.lon, 0.5, 0.5)
    return render_template('index.html', data=data, api_key=environ["APIKEY"])



if __name__ == '__main__':
    app.run()
