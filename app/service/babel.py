from flask import session, request
from flask_babel import Babel

from config import AVAILABLE_LANGUAGES


def config_babel(app):
    """Config babel for the application."""
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        if 'language' in session:
            return session['language']
        return request.accept_languages.best_match(AVAILABLE_LANGUAGES.keys())

    @app.before_request
    def before_request():
        session['language'] = get_locale()
