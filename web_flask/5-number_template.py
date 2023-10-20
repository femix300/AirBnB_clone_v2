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


@app.route('/c/<text>')
def c_text(text):
    """Returns 'c $text variable'"""
    text = escape(text).replace('_', ' ')
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Returns 'Python $text'"""
    text = escape(text).replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>')
def is_number(n):
    """Returns 'n is a number' if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays “Number: n” inside the tag BODY"""
    return render_template('5-template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
