from flask_wtf import FlaskForm
from financeapp.models import User
from wtforms import StringField, SubmitField, FormField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20, message='Username must be at least 5 characters and no more than 20')])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is not None:
            raise ValidationError("Username Taken!")
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first() is not None:
            raise ValidationError('Email Taken!')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
