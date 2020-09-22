import requests

api_token = 'btkmg5v48v6qjthfm1t0'
# API URL with formatable ticker
api_url = 'https://finnhub.io/api/v1/stock/metric?symbol={}&metric=all&token='
api_url_quote = 'https://finnhub.io/api/v1/quote?symbol={}&token='
request_json = requests.get(api_url.format('AAPL') + api_token).json()

tickers = ['AAPL', 'TSLA', 'GOOG', 'FB']

def getBeta(ticker):
  ticker_json = requests.get(api_url.format(ticker['Ticker']) + api_token).json()
  try:
    beta = ticker_json['metric']['beta']
  except:
    beta = 'N/A'
  return beta

def getMultipleBeta(arrayOfTickers):

  for ticker in arrayOfTickers:
    ticker['Beta'] = getBeta(ticker)

def getPrice(ticker):
  ticker_json = requests.get(api_url_quote.format(ticker['Ticker']) + api_token).json()
  try:
    price = ticker_json['c']
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



