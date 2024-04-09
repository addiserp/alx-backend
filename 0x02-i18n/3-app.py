#!/usr/bin/env python3
"""
    Starts a Flash-babel Web Application
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config(object):
    """
    Babel Configuration setup
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    home page index
    """
    return render_template('3-index.html')


@babel.locale_selector
def get_locale():
    """
    the Babel extension in Flask for locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
