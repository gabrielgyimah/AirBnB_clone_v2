#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def index():
        return "Hello HBNB!"

    @app.route("/hbnb", strict_slashes=False)
    def hbnb():
        return "HBNB"

    @app.route("/c/<text>", strict_slashes=False)
    def c(text):
        if "_" in text:
            text = text.replace("_", " ")
        return f"C {text}"

    @app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
    @app.route("/python/<text>", strict_slashes=False)
    def python(text):
        if "_" in text:
            text = text.replace("_", " ")
        return f"Python {text}"

    @app.route("/number/<int:n>", strict_slashes=False)
    def number(n):
        if isinstance(n, int):
            return f"{n} is a number"

    @app.route("/number_template/<int:n>", strict_slashes=False)
    def number_template(n):
        if isinstance(n, int):
            return render_template("5-number.html", n=n)

    app.run(host="0.0.0.0", port=5000, debug=True)
