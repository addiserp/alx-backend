#!/usr/bin/env python3
'''
Task 5: a user login system
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''
    Babel Configuration setup
    '''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Gets a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    It cheacks before each request's resolution.
    """

    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    the Babel extension in Flask for locale

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''
    home page index

    Returns:
        html: homepage
    '''
    return render_template("5-index.html")


# uncomment this line and comment the @babel.localeselector
# you get this error:
# AttributeError: 'Babel' object has no attribute 'localeselector'
# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
