from flask import render_template, Blueprint

blog_blueprint = Blueprint('blog', __name__)


@blog_blueprint.route('/blog')
def index():
    return 'Not implemented'
