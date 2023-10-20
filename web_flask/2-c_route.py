#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def C_text(text):
    """Replace underscores with spaces in the text variable"""
    text = escape(text).replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)