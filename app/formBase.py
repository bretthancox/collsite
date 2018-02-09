from flask_wtf import FlaskForm as Form
from wtforms import validators, DateTimeField, SubmitField, StringField
from wtforms import RadioField, DateField
from wtforms import TextField as Tfield  #renamed to prevent overlap with CouchDB module
from wtforms import PasswordField as Pwfield

class bookingForm(Form):
	"""This class is used to construct the fields to be used in the form.
	The label (e.g. 'Name:') is used in the jinja template as 
	{{ form.name.label }} where 'form' is the instantiated class and 
	'name' is the object in this class. The form field (e.g. a TextField)
	is invoked through {{ form.name }} with the same meaning as above"""
	name = Tfield('Name:')
	email = Tfield('Email:')
	booking_date = StringField('Requested date:')#, format='%m/%d/%Y')  #Only defines what the field expects - a datepicker still needs to be in the HTML/JS
	booking_time = StringField('Requested time:')
    #booking_date = RadioField('Select time', choices=[('10', '10:00AM'), ('11', '11:00AM'), ('14', '2:00PM')])

class loginForm(Form):
       username = Tfield('Username:')
       password = Pwfield('Password:')
