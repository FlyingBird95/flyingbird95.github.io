from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import gettext as _


class LoginForm(FlaskForm):
    email = StringField(_('Your email'), validators=[DataRequired(), Email()])
    password = PasswordField(_('Your password'), validators=[DataRequired()])
    submit = SubmitField(_('Login'))
