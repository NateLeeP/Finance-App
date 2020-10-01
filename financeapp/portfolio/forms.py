from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, NumberRange
from wtforms import StringField, IntegerField, FieldList, SubmitField, FormField, BooleanField
import requests


class PortfolioEntry(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    shares = IntegerField('Number of shares', validators=[DataRequired(message='Must be a number.'), NumberRange(min=1)])
    def validate_ticker(self, ticker):
        if requests.get('https://sandbox.iexapis.com/stable/stock/' + ticker.data + '/book?token=Tpk_8ef08bcd612444eab903cf6d1877b2bb').status_code == 404:
            raise ValidationError(ticker.data + ' does not exist.')

class PortfolioHoldings(FlaskForm):

    holdings = FieldList(FormField(PortfolioEntry), validators=[DataRequired()], min_entries=1)
    submit = SubmitField('Submit Holdings')
    save_portfolio = BooleanField('Save Portolio?', default=True)
