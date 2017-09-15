from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from wtforms import DateField
from datetime import date

from wtforms.fields.html5 import DateField

class LoginForm(Form):
    """Login form to access writing and settings pages"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class StudentRegistrationForm(Form):
    """ Form to collect student registration data """
    firstname = StringField('First Name:',validators=[DataRequired()])
    middlename = StringField('Middle Name:',validators=[DataRequired()])
    lastname = StringField('Last Name:',validators=[DataRequired()])
    studentid = StringField('Student ID:',validators=[DataRequired()])
    dt = DateField('DatePicker', format='%Y-%m-%d')
    dob = DateField('Date of Birth:')
    address1 = StringField('Address 1:',validators=[DataRequired()])
    address2 = StringField('Address 2:')
    zipcode = StringField('Zip Code:',validators=[DataRequired()])
    state = StringField('State:',validators=[DataRequired()])
    grade = StringField('Grade:',validators=[DataRequired()])

class IncidentForm(Form):
    """ Form to report a new student incident"""
    location = StringField('Location :')
    teacher = StringField('Teacher:')
    minor = StringField('Minor problem behavior :')
    major = StringField('Major problem behavior :')
    motivation = StringField('Possible motivation :')
    action = StringField('Action Taken :')
    others = StringField('Others involved in the incident :')
    
class SearchForm(Form):
    search = StringField('txtSearch')
