from flask import Flask
from flask import render_template
from cafes import good_locations

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = []
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
