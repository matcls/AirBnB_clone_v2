#!/usr/bin/python3
"""
Hello Flask Module.

Starts a Flask web application.
Listens on 0.0.0.0  on port 5000.
Routes:
/: display “Hello HBNB!
hbnb: display “HBNB”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display “Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/", strict_slashes=False)
def hbnb():
    """Display “HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
