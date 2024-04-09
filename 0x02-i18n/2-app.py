#!/usr/bin/python3
"""
    Starts a Flash-babel Web Application
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    # ...
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    to determine the best match with our supported languages.

    Returns:
        str: best match
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
        index start point for 0x02. i18n
    """

    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
