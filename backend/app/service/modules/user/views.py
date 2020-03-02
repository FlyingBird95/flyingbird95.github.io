from flask import Blueprint, render_template, flash

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    flash('test')
    flash('Another test. This one is slightly longers')
    return render_template('admin.html')
