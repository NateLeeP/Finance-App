from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import current_user
from financeapp import db
from financeapp.portfolio.forms import PortfolioHoldings
from financeapp.models import User, Holding, Portfolio
from financeapp.util_functions import betaFunctions

portfolio_blueprint = Blueprint('portfolio_blueprint', __name__)

@portfolio_blueprint.route('/portfolio', methods=["POST", "GET"])
def portfolio():
    #holdings = [{'ticker':'TSLA','shares':20}, {'ticker':'GOOG', 'shares':40}]
    form=PortfolioHoldings()
    if request.method == 'GET':
        #logger.info('Hello')
        if current_user.is_authenticated:
            u = User.query.filter_by(id=current_user.get_id()).first()
            if u.portfolios:
                p = u.portfolios.first()
                form = PortfolioHoldings(obj = p)
        return render_template('portfolio.html', title='Portfolio',form=form)
    #if current_user.is_authenticated:
    #  u = User.query.filter_by(id=current_user.get_id()).first()
    #  if u.portfolios.first() is not None:
    #    p = u.portfolios.first()
    #    form = PortfolioHoldings(obj=p)
    #  else:
    #      p = Portfolio(investor=u)
    #      form = PortfolioHoldings(obj=p)
    if form.validate_on_submit():
      if current_user.is_authenticated and form.save_portfolio.data:
        u = User.query.filter_by(id=current_user.get_id()).first()
        p = u.portfolios.first()
        if p:
          for holding in p.holdings.all():
            db.session.delete(holding)
        else:
          p = Portfolio(investor = u)
          db.session.add(p)
        for holding in form.holdings:
          h = Holding(ticker=holding.ticker.data, shares=holding.shares.data, portfolio=p)
          db.session.add(h)
        db.session.commit()
      tickers = [{'Ticker':subform.ticker.data, 'Shares':subform.shares.data} for subform in form.holdings]
      betaFunctions.updateTickerList(tickers, -56)
      calculations = betaFunctions.portfolioCalculations(tickers, True)
      #betaFunctions.getCAPM(tickers, -34)
      #new_calculations = betaFunctions.portfolioCalculations(tickers, False)
      return render_template('portfoliotest.html', form=form, betas=tickers, calculations=calculations)
    else:
        return render_template('portfolio.html', title='Portfolio', form=form)

@portfolio_blueprint.route('/disclaimer', methods=["GET"])
def disclaimer():
    return render_template('calculationDisclaimer.html')