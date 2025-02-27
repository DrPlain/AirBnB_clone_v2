#!/usr/bin/python3
""" Starts a Flask web application listeninig on 0.0.0.0:5000"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Displays 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun(text):
    """Prints C followed by <text> content"""
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays Python followed by <text> content"""
    text = text.replace('_', ' ')
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
