import os
import click

from app.service.database import db
from app.service.modules.user.models import User


def add_commands(app):
    add_translate_commands(app)
    add_db_commands(app)


def add_translate_commands(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel init -i messages.pot -d translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')

    @translate.command()
    def update():
        """Update all languages."""
        if os.system('pybabel extract -F babel.cfg -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d translations'):
            raise RuntimeError('compile command failed')


def add_db_commands(app):
    @app.cli.group()
    def database():
        """Database creation and deletion commands."""
        pass

    @database.command()
    def create():
        """Creates all the models."""
        db.create_all()

    @database.command()
    def populate():
        """Populate the database."""
        session = db.session()
        user = User(email="admin@test.nl")
        user.set_password("asdasd")
        session.add(user)

        session.commit()

    @database.command()
    def drop():
        """Deletes all the models."""
        db.drop_all()
