#!/usr/bin/python3
"""
Starts a Flask web application.
Listens on 0.0.0.0  on port 5000.
Routes:
  *  /states: Display a HTML page with the list of all State objects.
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage.
        sorted by name (A->Z)
          LI tag: description of one State: <state.id>: <B><state.name></B>
  *  /states/<id>: Display a HTML page with the list of City objects
    linked to the State sorted by name (A->Z).
    If a State object is found whit this id:
        H1 tag: “State: ”
        H1 tag: “State: ”
        UL tag: with the list of City objects linked to the State.
        sorted by name (A->Z)
          LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: “Not found!”
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all States in DBStorage.
    """
    states=storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
