#!/usr/bin/python3
"""starts a Flask web application; listens on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/states", strict_slashes=False)
    def display_states():
        """Render state_list html page to display States created"""
        states = storage.all(State)

        return render_template('7-states_list.html', states=states)

    @app.route("/states/<id>", strict_slashes=False)
    def display_state(id):
        """Serves an HTML page populated with data of a State"""
        states = storage.all(State)
        cities = storage.all(City)
        
        for state in states:
            if state == "States."+id:
                return render_template("9-states.html", id=id, states=states, cities=cities)
        return render_template("9-states.html")

    def teardown(self):
        """Method to remove current SQLAlchemy Session"""
        storage.close()

    app.run(host="0.0.0.0", port=5000, debug=True)
