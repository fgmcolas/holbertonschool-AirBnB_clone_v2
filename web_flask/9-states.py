#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all State objects"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_id(id):
    """Display a HTML page with details of a State object"""
    all_states = storage.all(State).values()
    for state in all_states:
        if state.id == id:
            return render_template('9-states.html', selected_state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)