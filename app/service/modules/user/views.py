from flask import Blueprint, render_template, flash, request
from flask_babel import lazy_gettext as _

from app.service.modules.user.forms import LoginForm
from app.service.modules.user.models import User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.from_email(email=form.email.data)
        if user is None or not user.check_password(form.password.data):
            flash(_("Username not found, or the given password is incorrect."), category="error")
        else:
            flash(_("Welcome"))
    return render_template('admin.html', form=form)
