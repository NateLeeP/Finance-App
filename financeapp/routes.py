from financeapp import app, db
from financeapp.models import User, Portfolio, Holding
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from financeapp import stock_prices
from financeapp import betaFunctions
from financeapp.forms import StockForm, PortfolioHoldings, RegistrationForm, LoginForm, PortfolioEntry
from financeapp import dateLookUp
import random
import datetime
import logging

#logger = logging.getLogger(__name__)

# Testing chart, not to be used as home page.
#@app.route('/home', methods=['GET', 'POST'])
#def home():
#    stock1 = 'TSLA'
#    stock2 = 'GOOG'
#    test = 'GOOG'
#    date = 'Aug {}, 2020'
#    labels = [date.format(i) for i in range(1, 31)]
#    data = [random.uniform(-2, 2) for i in range(1, 31)]
#    data2 = [random.uniform(-2, 2) for i in range(1, 31)]
#    return render_template('home.html', title="Home", legend=test, data=data, data2=data2, labels=labels, stock1=stock1, stock2=stock2)






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
