from config import AVAILABLE_LANGUAGES


def set_jinja_env(app):
    app.jinja_env.trim_blocks = True
    app.jinja_env.policies['ext.i18n.trimmed'] = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.globals.update(AVAILABLE_LANGUAGES=AVAILABLE_LANGUAGES)
