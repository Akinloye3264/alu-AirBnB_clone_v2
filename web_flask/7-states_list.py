#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display an HTML page with a list of all State objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_temp_
