import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError


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