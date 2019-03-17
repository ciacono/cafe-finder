from flask import Flask
from flask import render_template
from cafes import good_locations
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = good_locations(43.64469, -79.37996568810948, 50, 2.5)
    # lat, long, busy_pref, rating_pref
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()



