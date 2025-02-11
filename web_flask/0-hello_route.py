#!/usr/bin/python3
"""
This is a script that start a flask web app that listen on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
