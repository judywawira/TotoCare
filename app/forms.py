from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from wtforms import DateField
from datetime import date


class LoginForm(Form):
    """Login form to access writing and settings pages"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class DateForm(Form):
    """Date widget """
    dt = DateField('Pick a Date', format="%m/%d/%Y")

class StudentRegistrationForm(Form):
    """ Form to collect student registration data """
    firstname = StringField('First Name:',validators=[DataRequired()])
    middlename = StringField('Middle Name:',validators=[DataRequired()])
    lastname = StringField('Last Name:',validators=[DataRequired()])
    studentid = StringField('Student ID:',validators=[DataRequired()])
    dt = DateField('Date of Birth:', format="%m/%d/%Y")
    #DOB = StringField('Date of Birth:',validators=[DataRequired()])
    #DOB = DateField('Pick a Date', format="%m/%d/%Y")
    address1 = StringField('Address 1:',validators=[DataRequired()])
    address2 = StringField('Address 2:')
    zipcode = StringField('Zip Code:',validators=[DataRequired()])
    state = StringField('State:',validators=[DataRequired()])

