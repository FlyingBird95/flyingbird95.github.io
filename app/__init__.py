from flask import Flask

from app.cli import add_commands
from app.service.babel import config_babel
from app.service.database import config_db
from app.service.jinja_env import set_jinja_env
from app.service.modules.blog.views import blog_blueprint
from app.service.modules.main.views import main_blueprint
from app.service.modules.user.views import user_blueprint


def create_app(config_class="config.Config"):
    flask_app = Flask(__name__, static_folder='static/dist')
    flask_app.config.from_object(config_class)
    set_jinja_env(flask_app)
    config_babel(flask_app)
    add_commands(flask_app)
    config_db(flask_app)

    # Register modules
    flask_app.register_blueprint(blog_blueprint)
    flask_app.register_blueprint(main_blueprint)
    flask_app.register_blueprint(user_blueprint)

    # import models
    import app.service.modules.blog.models
    import app.service.modules.user.models

    return flask_app


if __name__ == '__main__':
    create_app("config.Config").run()
