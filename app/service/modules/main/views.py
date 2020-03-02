from flask import session, redirect, url_for, render_template, Blueprint, flash, request
from flask_babel import gettext as _

from app.service.modules.main.forms import ContactForm
from config import AVAILABLE_LANGUAGES

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/lang/<language_code>')
def set_language(language_code):
    if language_code not in AVAILABLE_LANGUAGES.keys():
        language_code = AVAILABLE_LANGUAGES.keys()[0]
    session['language'] = language_code
    return redirect(url_for('main.index'))


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            flash(_('Thanks for contacting me'))
        else:
            flash(_('There are some errors. Please fix them below.'), category="error")
    return render_template('index.html', form=form)
