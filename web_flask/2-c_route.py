#!/usr/bin/python3
"""
Starts a Flask web application.
Listens on 0.0.0.0  on port 5000.
Routes:
    *   /: display “Hello HBNB!
    *    hbnb: display “HBNB”
    *    /c/<text>: display “C ” followed by the value of the text
         variable (replace underscore _ symbols with a space ).
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display “Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display “HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
