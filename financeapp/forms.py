from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class StockForm(FlaskForm):
    ticker1 = StringField('Ticker One', validators=[DataRequired(), Length(min=1, max=5)])
    ticker2 = StringField('Ticker Two', validators=[DataRequired(), Length(min=1, max=5)])
    timeFrame = SelectField('Time Frame', choices=[('ytd', 'Year-to-Date'), ('1mo', 'One Month')])
    submit = SubmitField('Update Graph')
