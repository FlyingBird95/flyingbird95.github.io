import os
from collections import namedtuple

from flask_babel import lazy_gettext as _

Language = namedtuple('language', ['filename', 'name'])

AVAILABLE_LANGUAGES = {
    'en': Language(filename='images/en.jpg', name=_('English')),
    'nl': Language(filename='images/nl.png', name=_('Dutch')),
}


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'very_secret')
    BABEL_TRANSLATION_DIRECTORIES = '../translations'
    BABEL_DEFAULT_LOCALE = 'en'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/patrick.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
