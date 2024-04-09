#!/usr/bin/env python3
'''
Task 4: Force locale with URL parameter
'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''
    It's a config class
    '''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# @babel.localeselector
def get_locale() -> str:
    """
    It retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@app.route('/')
def index() -> str:
    '''
    It's a default route

    Returns:
        html: homepage
    '''
    return render_template("4-index.html")

# uncomment this line and comment the @babel.localeselector
# you get this error:
# AttributeError: 'Babel' object has no attribute 'localeselector'
babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()