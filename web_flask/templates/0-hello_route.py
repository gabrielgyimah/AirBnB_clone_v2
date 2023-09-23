#!/usr/bin/python3
"""Starts a Flask Web Server"""

from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello HBNB!"
    app.run(host='0.0.0.0', port=5000)
