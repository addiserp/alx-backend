#!/usr/bin/env python3
"""
    Starts a Flash Web Application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
        index start point for 0x02. i18n
    """

    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True)
