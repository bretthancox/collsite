from flask_wtf import Form
from wtforms import StringField, BooleanField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    date_pick = DateTimeField('date_picked', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
