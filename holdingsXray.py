import requests
import yfinance

# Sample data from API
data = requests.get('https://eodhistoricaldata.com/api/fundamentals/VTI.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX').json()

# Function will receive list of holdings with 'ticker', 'shares'
holdings = [{'Ticker':'AAPL', 'shares':100}, {'Ticker':'TSLA', 'shares':40}, {'Ticker':'FB', 'shares': 30}, {'Ticker':'VTI', 'shares':150}]

vti_holdings = [{'Ticker':'AAPL', 'Asset_%':5.8}, {'Ticker': 'TSLA', 'Asset_%':4.5}, {'Ticker':'GOOG', 'Asset_%':3.6}, {'Ticker':'FB', 'Asset_%':2.8}, {'Ticker':'AMZN', 'Asset_%':2.2}]

print(holdings)

# Function to process holdings
def topHoldings(holdings):
  for holding in holdings:
    # Calculate market value according to most recent price.
    price = yfinance.Ticker(holding['Ticker']).history(period='1d').T.loc['Open'][0]
    holding['Market_Value'] = price * holding['shares']
  # Market value of portfolio.
  total_market_value = sum([holding.get('Market_Value') for holding in holdings])
  print(total_market_value)
  holdings.sort(key=lambda x: x['Market_Value'] / total_market_value, reverse=True)
  return holdings







print('\n', topHoldings(holdings))