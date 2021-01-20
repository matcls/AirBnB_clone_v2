#!/usr/bin/python3
"""
Hello Flask Module.

Starts a Flask web application.
Listens on 0.0.0.0  on port 5000.
Routes:
/: display “Hello HBNB!
"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Start a Flask web application."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
