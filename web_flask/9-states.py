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
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/", defaults={"id": None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """Display a HTML page with details of a State object"""
    states = storage.all(State).values()
    if id:
        state_by_id = None
        for state in states:
            if state.id == id:
                state_by_id = state
        return render_template('9-states.html', state=state_by_id, id=id)
    else:
        return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
