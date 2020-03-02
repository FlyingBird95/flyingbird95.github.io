from flask import Flask

from app.cli import add_commands
from app.service.babel import config_babel
from app.service.database import config_db
from app.service.jinja_env import set_jinja_env
from app.service.modules.blog.views import blog_blueprint
from app.service.modules.main.views import main_blueprint
from app.service.modules.user.views import user_blueprint


def create_app(config_class="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    add_commands(app)
    set_jinja_env(app)
    config_babel(app)
    config_db(app)

    # Register modules
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)

    # import models
    import app.service.modules.blog.models

    return app
