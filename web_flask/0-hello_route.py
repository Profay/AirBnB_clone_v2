#!/usr/bin/python3
# a script that starts a Flask web application with port 5000

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ print hello world """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)