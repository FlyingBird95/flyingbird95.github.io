from config import AVAILABLE_LANGUAGES


def set_jinja_env(app):
    app.jinja_env.globals.update(AVAILABLE_LANGUAGES=AVAILABLE_LANGUAGES)
