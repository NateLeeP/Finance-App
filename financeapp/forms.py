from flask_wtf import FlaskForm
from financeapp.models import User
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField, FieldList, FormField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange, Email, EqualTo
import requests










"""
08.25.2020: Form was used for 'custom' route. Route no longer necessary

class StockFormCustomTime(FlaskForm):
    ticker1 = StringField('Ticker One', validators=[DataRequired(), Length(min=1, max=5)])
    ticker2 = StringField('Ticker Two', validators=[DataRequired(), Length(min=1, max=5)])
    start = StringField('Start Date', validators=[DataRequired()])
    end = StringField('End Date', validators=[DataRequired()])
    submit = SubmitField('Update Graph')

"""