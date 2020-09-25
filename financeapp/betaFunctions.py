import requests

#api_token = 'btkmg5v48v6qjthfm1t0'
api_token = 'pk_8d0f8e5a2a134ad48410c868b4849d70'
# API URL with formatable ticker
#api_url = 'https://finnhub.io/api/v1/stock/metric?symbol={}&metric=all&token='
api_url_price = 'https://cloud.iexapis.com/stable/stock/{}/quote/latestPrice?token='
#api_url_quote = 'https://finnhub.io/api/v1/quote?symbol={}&token='
api_url_beta = 'https://cloud.iexapis.com/stable/stock/{}/stats/beta?token='

tickers = ['AAPL', 'TSLA', 'GOOG', 'FB']

def getBeta(ticker):
  ticker_json = requests.get(api_url_beta.format(ticker['Ticker']) + api_token).json()
  try:
    beta = ticker_json
  except:
    beta = 'N/A'
  return beta

def getMultipleBeta(arrayOfTickers):

  for ticker in arrayOfTickers:
    ticker['Beta'] = getBeta(ticker)

def getPrice(ticker):
  ticker_json = requests.get(api_url_price.format(ticker['Ticker']) + api_token).json()
  try:
    price = ticker_json
  except:
    price = 'N/A'

  return price

def getMultiplePrice(arrayOfTickers):
  for ticker in arrayOfTickers:
    ticker['Market_Value'] = getPrice(ticker) * ticker['Shares']

def getPortfolioValue(arrayOfTickers):
  totalPortfolioValue = sum([ticker['Market_Value'] for ticker in arrayOfTickers])
  return totalPortfolioValue

def getPortfolioPercentage(arrayOfTickers, portfolioValue):
  for ticker in arrayOfTickers:
    ticker['%_of_Portfolio'] = ticker['Market_Value'] / portfolioValue

def getCAPM(arrayOfTickers, expectedMarketReturn):
  for ticker in arrayOfTickers:
    # Expected return using CAPM. Formula for CAPM is Expected Return = Risk-Free Rate + Beta(Expected Market Return - Risk-Free Rate)
    # Interest rate on three-month U.S. treasury bill is 'risk-free rate'.
    # Current risk-free rate is 0.10%
    # Market Return as percentage
    ticker['Expected_Return'] = .10 + ticker['Beta'] * (expectedMarketReturn - 0.10)

def portfolioExpectedReturn(arrayOfTickers):
  totalExpectedReturn = 0
  for ticker in arrayOfTickers:
    totalExpectedReturn += ticker['%_of_Portfolio'] * ticker['Expected_Return']

  return totalExpectedReturn

def calculateRequiredReturn(new_portfolio_value, old_portfolio_value):
  requiredReturn = (float(new_portfolio_value) / float(old_portfolio_value)) - 1
  requiredReturn *= 100
  return requiredReturn