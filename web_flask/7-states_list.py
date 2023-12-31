#!/usr/bin/python3
"""starts a Flask web application; listens on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/states", strict_slashes=False)
    def display_states():
        """Render state_list html page to display States created"""
        states = storage.all(State)
        return render_template('7-states_list.html', states=states)

    @app.teardown_appcontext
    def teardown(self):
        """Method to remove current SQLAlchemy Session"""
        storage.close()

    app.run(host="0.0.0.0", port=5000, debug=True)
