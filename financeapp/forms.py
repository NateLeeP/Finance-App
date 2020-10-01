from flask_wtf import FlaskForm
from financeapp.models import User
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField, FieldList, FormField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange, Email, EqualTo
import requests

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


class StockForm(FlaskForm):
    ticker1 = StringField('Ticker One', validators=[DataRequired(), Length(min=1, max=5,message='Ticker must be between 1-5 characters')])
    ticker2 = StringField('Ticker Two', validators=[DataRequired(), Length(min=1, max=5, message='Ticker must be between 1-5 characters')])
    timeFrame = SelectField('Time Frame', choices=[('ytd', 'Year-to-Date'), ('1mo', 'One Month'), ('5d', 'One Week'),
                                                   ('6mo', 'Six Months'), ('1y', 'One Year'), ('5y', 'Five Years'), ('max', 'Since inception'), ('custom', 'Custom')])
    start = StringField('Start Date')
    end = StringField('End Date')
    submit = SubmitField('Update Graph')

    def validate_ticker1(self, ticker1):
        if requests.get('https://sandbox.iexapis.com/stable/stock/' + ticker1.data + '/book?token=Tpk_8ef08bcd612444eab903cf6d1877b2bb').status_code == 404:
            raise ValidationError(ticker1.data + ' ticker does not exist.')

    def validate_ticker2(self, ticker2):
        if requests.get('https://sandbox.iexapis.com/stable/stock/' + ticker2.data + '/book?token=Tpk_8ef08bcd612444eab903cf6d1877b2bb').status_code == 404:
            raise ValidationError(ticker2.data + ' does not exist.')


class PortfolioEntry(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    shares = IntegerField('Number of shares', validators=[DataRequired(message='Must be a number.'), NumberRange(min=1)])
    def validate_ticker(self, ticker):
        if requests.get('https://sandbox.iexapis.com/stable/stock/' + ticker.data + '/book?token=Tpk_8ef08bcd612444eab903cf6d1877b2bb').status_code == 404:
            raise ValidationError(ticker.data + ' does not exist.')

class PortfolioHoldings(FlaskForm):

    holdings = FieldList(FormField(PortfolioEntry), validators=[DataRequired()], min_entries=1)
    submit = SubmitField('Submit Holdings')







"""
08.25.2020: Form was used for 'custom' route. Route no longer necessary

class StockFormCustomTime(FlaskForm):
    ticker1 = StringField('Ticker One', validators=[DataRequired(), Length(min=1, max=5)])
    ticker2 = StringField('Ticker Two', validators=[DataRequired(), Length(min=1, max=5)])
    start = StringField('Start Date', validators=[DataRequired()])
    end = StringField('End Date', validators=[DataRequired()])
    submit = SubmitField('Update Graph')

"""