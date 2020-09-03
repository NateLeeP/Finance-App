from financeapp import app
from flask import render_template, redirect, url_for
from financeapp import stock_prices
from financeapp.forms import StockForm
import random
import datetime

# Testing chart, not to be used as home page.
@app.route('/home', methods=['GET', 'POST'])
def home():
    stock1 = 'TSLA'
    stock2 = 'GOOG'
    test = 'GOOG'
    date = 'Aug {}, 2020'
    labels = [date.format(i) for i in range(1, 31)]
    data = [random.uniform(-2, 2) for i in range(1, 31)]
    data2 = [random.uniform(-2, 2) for i in range(1, 31)]
    return render_template('home.html', title="Home", legend=test, data=data, data2=data2, labels=labels, stock1=stock1, stock2=stock2)



@app.context_processor
def utility_processor():
    def scale_unit(timeFrame):
        if (timeFrame == '1mo' or timeFrame == '5d'):
            return 'day'
        elif (timeFrame == 'ytd' or timeFrame == '6mo' or timeFrame == '1y'):
            return 'month'
        else:
            return 'year'

    return dict(scale_unit=scale_unit)


@app.route('/')
@app.route('/chart', methods=["POST", "GET"])
def chart():
    form = StockForm()
    if form.validate_on_submit(): #Validate wtf_forms validators
        #if form.timeFrame.data == 'custom':
        #    return redirect(url_for('customTime')
        return render_template('chartV2.html', title='Chart', form=form)

    else:
        form.ticker1.data = "TSLA"
        form.ticker2.data = "GOOG"
        form.timeFrame.data = "ytd"
        return render_template('chartV2.html', title='Chart', form=form)


@app.context_processor
def utility_processor():
    def stock_dates_combine(ticker, timeFrame='ytd', start=None, end=None):
        return stock_prices.stock_dates_combine(ticker, timeFrame, start, end)
    return dict(stock_dates_combine=stock_dates_combine)

@app.context_processor
def utility_processor():
    def stock_prices_combine(ticker, timeFrame='ytd', start=None, end=None):
        return stock_prices.stock_prices_combine(ticker, timeFrame, start, end) # 08.24.2020 Notice: Do not have to pass the defaults a second time!!
    return dict(stock_prices_combine=stock_prices_combine)


"""
08.24.2020: No longer need these functions. One function handles prices/dates for predefined and custom date ranges.
@app.context_processor
def utility_processor():
    def stock_price_ytd(ticker, timeFrame):
        return stock_prices.stock_price_ytd(ticker, timeFrame)
    return dict(stock_price_ytd=stock_price_ytd)

@app.context_processor
def utility_processor():
    def stock_dates_ytd(ticker, timeFrame):
        return stock_prices.stock_dates_ytd(ticker, timeFrame)
    return dict(stock_dates_ytd=stock_dates_ytd)


@app.context_processor
def utility_processor():
    def stock_price_custom(ticker, start, end):
        return stock_prices.stock_price_custom(ticker, start, end)
    return dict(stock_price_custom=stock_price_custom)

@app.context_processor
def utility_processor():
    def stock_dates_custom(ticker, start, end):
        return stock_prices.stock_dates_custom(ticker, start, end)
    return dict(stock_dates_custom=stock_dates_custom)
"""



"""
08.24.2020: No longer need this route, 'chart' route now handles custom date range
@app.route('/chart/customTime', methods=["POST", "GET"])
def customTime():
    form = StockFormCustomTime()
    if form.validate_on_submit():
        return render_template('chartCustomTime.html', form=form)
    #form.ticker1.data = stockForm.ticker1.data
    #form.ticker2.data = stockForm.ticker2.data
    #if form.validate_on_submit():
    else:
        form.ticker1.data = 'TSLA'
        form.ticker2.data = 'GOOG'
        form.start.data = '2020-08-10'
        form.end.data = '2020-08-16'
        return render_template('chartCustomTime.html', title='Chart Custom', form=form)
"""
# Previous code
"""
    form = StockForm()
    if form.validate_on_submit():
        ticker1 = form.ticker1.data
        ticker2 = form.ticker2.data
        dates, prices = stock_prices.stock_price_ytd(ticker1)
        dates2, prices2 = stock_prices.stock_price_ytd(ticker2)
        return render_template('chart.html', title='Chart', dates=dates, prices=prices,prices2=prices2, ticker=ticker1, ticker2=ticker2, form=form)
        #return redirect(url_for("chart")) Do I NEED to use redirect here?
    else:
        ticker1 = "TSLA"
        ticker2 = "AMZN"
        dates, prices = stock_prices.stock_price_ytd(ticker1)
        dates2, prices2 = stock_prices.stock_price_ytd(ticker2)
        return render_template('chart.html', title='Chart', dates=dates, prices=prices,prices2=prices2, ticker=ticker1, ticker2=ticker2, form=form)
"""
