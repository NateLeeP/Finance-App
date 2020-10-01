from flask import Blueprint, render_template
from financeapp.chart.forms import StockForm
from financeapp.util_functions import stock_prices

chart_blueprint = Blueprint('chart_blueprint', __name__)


@chart_blueprint.context_processor
def utility_processor():
    def scale_unit(timeFrame):
        if (timeFrame == '1mo' or timeFrame == '5d'):
            return 'day'
        elif (timeFrame == 'ytd' or timeFrame == '6mo' or timeFrame == '1y'):
            return 'month'
        else:
            return 'year'

    return dict(scale_unit=scale_unit)

@chart_blueprint.context_processor
def stock_date_processor():
    def stock_dates_combine(ticker, timeFrame='ytd', start=None, end=None):
        return stock_prices.stock_dates_combine(ticker, timeFrame, start, end)
    return dict(stock_dates_combine=stock_dates_combine)

@chart_blueprint.context_processor
def stock_price_processor():
    def stock_prices_combine(ticker, timeFrame='ytd', start=None, end=None):
        return stock_prices.stock_prices_combine(ticker, timeFrame, start, end) # 08.24.2020 Notice: Do not have to pass the defaults a second time!!
    return dict(stock_prices_combine=stock_prices_combine)

@chart_blueprint.route('/', methods=["GET", "POST"])
@chart_blueprint.route('/chart', methods=["GET", "POST"])
def chart():
    form = StockForm()
    if form.validate_on_submit(): #Validate wtf_forms validators
        #    if form.timeFrame.data == 'custom':
        #    return redirect(url_for('customTime')
        return render_template('chart.html', title='Chart', form=form)

    else:
        form.ticker1.data = "TSLA"
        form.ticker2.data = "GOOG"
        form.timeFrame.data = "ytd"
        return render_template('chart.html', title='Chart', form=form)