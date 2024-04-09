#!/usr/bin/python3
"""
    Starts a Flash-babel Web Application
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    # ...
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
        index start point for 0x02. i18n
    """

    return render_template('1-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
