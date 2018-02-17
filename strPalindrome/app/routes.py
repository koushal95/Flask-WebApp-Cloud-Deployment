from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import formPage


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = formPage()
    if form.validate_on_submit():
        strin = form.stringInput.data
        strin = strin.casefold()
        revstr = reversed(strin)
        if list(strin) == list(revstr):
            flash('The string {} is palindrome'.format(form.stringInput.data), 'success')
        else:
            flash('The string {} is not palindrome'.format(form.stringInput.data), 'danger')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

