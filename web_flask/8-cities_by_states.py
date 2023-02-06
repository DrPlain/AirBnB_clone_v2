#!/usr/bin/python3
"""Fetches data from storage engine and displays in li tag
Listens on 0.0.0.0:5000

"""
from models import storage, storage_type
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays html page of cities by states in a list format"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
