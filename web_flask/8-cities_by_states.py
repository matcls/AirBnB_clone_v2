#!/usr/bin/python3
"""
Starts a Flask web application.
Listens on 0.0.0.0  on port 5000.
Routes:
  *  /cities_by_states: HTML page with the list of all State objects
     present in DBStorage sorted by name.
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage.
        sorted by name (A->Z)
          LI tag: description of one State: <state.id>: <B><state.name></B>
          + UL tag: with the list of City objects linked to the State.
             LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State and related cities
       in DBStorage.
    """
    return render_template("8-cities_by_states.html",
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
