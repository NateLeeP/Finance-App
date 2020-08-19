from financeapp import app
from flask import render_template, redirect, url_for
from financeapp import stock_prices
from financeapp.forms import StockForm
import random

@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
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
    def stock_price_ytd(ticker, timeFrame):
        return stock_prices.stock_price_ytd(ticker, timeFrame)
    return dict(stock_price_ytd=stock_price_ytd)

@app.context_processor
def utility_processor():
    def stock_dates_ytd(ticker, timeFrame):
        return stock_prices.stock_dates_ytd(ticker, timeFrame)
    return dict(stock_dates_ytd=stock_dates_ytd)

@app.route('/chart', methods=["POST", "GET"])
def chart():
    form = StockForm()
    if form.validate_on_submit():
        return render_template('chartV2.html', title='Chart', form=form)
    else:
        form.ticker1.data = "TSLA"
        form.ticker2.data = "GOOG"
        form.timeFrame.data = "ytd"
        return render_template('chartV2.html', title='Chart', form=form)







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
