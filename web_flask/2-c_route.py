#!/usr/bin/python3
"""
This script initiates a Flask web application:
Accessible on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Handle requests to the root URL ('/') and returns a greeting string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles requests to the '/hbnb' URL and returns a string."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Handles requests to the '/c/<text>' URL and returns a string with
    'C' followed by the text parameter."""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
