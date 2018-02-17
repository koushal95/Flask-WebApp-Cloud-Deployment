from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class formPage(FlaskForm):
    stringInput = StringField('String Input', validators=[DataRequired()])
    submit = SubmitField('Check This')