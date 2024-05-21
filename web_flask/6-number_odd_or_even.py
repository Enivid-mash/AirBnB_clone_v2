#!/usr/bin/python3
"""
This script initiates a Flask web application:
Accessible on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
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


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Handles requests to the '/python' or '/python/<text>' URL and returns
    a string with 'Python' followed by the text parameter."""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Handles requests to the '/number/<int:n>' URL and returns a string
    confirming that 'n' is a number."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Handles requests to the '/number_template/<int:n>' URL and returns
    an HTML page only if 'n' is an integer."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Handles requests to the '/number_odd_or_even/<int:n>' URL and returns
    an HTML page indicating if 'n' is odd or even."""
    eo = "odd" if n % 2 else "even"
    return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
