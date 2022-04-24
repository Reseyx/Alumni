from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email, DataRequired

class SignUp(FlaskForm):
  firstname = StringField('firstname', validators=[InputRequired()])
  lastname = StringField('lastname', validators=[InputRequired()])
  email = StringField('email', validators=[InputRequired()])
  password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm  = PasswordField('Repeat Password')
  faculty = StringField('faculty', validators=[InputRequired()])
  department = StringField('department', validators=[InputRequired()])
  programme = StringField('programme', validators=[InputRequired()])
  graduationyear = StringField('graduationyear', validators=[InputRequired()])
  currentjob = StringField('currentjob', validators=[InputRequired()])
  submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})
  
class LogIn(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class SearchForm(FlaskForm):       
  searched=StringField("searched",validators=[DataRequired()])
  submit= SubmitField("submit")