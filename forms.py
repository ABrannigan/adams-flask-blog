from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators = [DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators = [DataRequired(), Email()])

    password = PasswordField('Password',
                            validators = [DataRequired(), Length(min=8, max=20)])

    confirm_password = PasswordField('Password',
                            validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(), Email()])

    password = PasswordField('Password',
                            validators = [DataRequired(), Length(min=8, max=20)])

    # rember allows users to stay logged in for some time after browser closes uses secure cookie
    remember = BooleanField('Rember Me')

    submit = SubmitField('Login')
