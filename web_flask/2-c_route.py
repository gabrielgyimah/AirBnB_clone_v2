#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask


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

    app.run(host="0.0.0.0", port=5000)
