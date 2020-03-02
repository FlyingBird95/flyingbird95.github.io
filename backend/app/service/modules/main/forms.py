from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_babel import gettext as _


class ContactForm(FlaskForm):
    name = StringField(_('Your name'), validators=[DataRequired()])
    email = StringField(_('Your email'), validators=[DataRequired(), Email()])
    subject = StringField(_('Subject'), validators=[DataRequired()])
    message = TextAreaField(_('Your message'), validators=[DataRequired()])
    submit = SubmitField(_('Send message'))
