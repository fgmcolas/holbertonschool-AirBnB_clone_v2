#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with the list of states and their cities"""
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
