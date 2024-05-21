#!/usr/bin/python3
"""
This script initiates a Flask web application:
Accessible on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return the string Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
