import yfinance


def parse_dates(ticker_df):
    dates = ticker_df.index
    return list(dates.strftime("%B %d, %Y")) # Convert index to "Month Day, Year" format. Convert to list after.

def parse_prices(ticker_df):
    prices = ticker_df['Close'] # Using 'Close' to represent price
    prices = percent_change(prices)
    prices = cum_sum(prices)
    return list(prices) # return as list


def percent_change(series):
    # Accepts dataframe series and returns a list
    percent_change_data = []
    for i in range(len(series.index)):  # Adjust from series.index to range(len(series.index))
        if i == 0:  # Special case for 'zero' index
            percent_change_data.append(0)
        else:

            percent_change_data.append(
                ((series[i] - series[i - 1]) / series[0]) * 100)  # new - old / baseline. Keep same baseline
            # Adjusted series.index. Why? Index was in string. An integer cannot be subtracted from a string
    return percent_change_data

def cum_sum(numbers):
    # Accepts a list of numbers as a parameter and returns the cumulative sum
    cum_sum = []
    for i in range(len(numbers)):
        if (i == 0):
            cum_sum.append(numbers[i])
        else:
            cum_sum.append(numbers[i] + cum_sum[i-1])
    return cum_sum

def stock_price_ytd(ticker, timeFrame):
    # Separated price and date into two different functions. Attempting to get functions to work in Jinja template.
    ticker = yfinance.Ticker(ticker)
    # ticker_name = ticker.info['longName'] Attempt to pull in names, but not all tickers had info attribute
    ticker_df = ticker.history(period=timeFrame)
    dates = parse_dates(ticker_df)
    prices = parse_prices(ticker_df)
    return prices # ticker_name

def stock_dates_ytd(ticker, timeFrame):
    ticker = yfinance.Ticker(ticker)
    ticker_df = ticker.history(period=timeFrame)
    dates = parse_dates(ticker_df)
    return dates

def stock_price_custom(ticker, start, end):
    # Separated price and date into two different functions. Attempting to get functions to work in Jinja template.
    ticker = yfinance.Ticker(ticker)
    # ticker_name = ticker.info['longName'] Attempt to pull in names, but not all tickers had info attribute
    ticker_df = ticker.history(start=start, end=end)
    dates = parse_dates(ticker_df)
    prices = parse_prices(ticker_df)
    return prices # ticker_name

def stock_dates_custom(ticker, start, end):
    ticker = yfinance.Ticker(ticker)
    ticker_df = ticker.history(start=start, end=end)
    dates = parse_dates(ticker_df)
    return dates


def stock_dates_combine(ticker, timeFrame='ytd', start=None, end=None):
    ticker = yfinance.Ticker(ticker)
    if start and end:
        ticker_df = ticker.history(start=start, end=end)
        dates = parse_dates(ticker_df)
        return dates
    else:
        ticker_df = ticker.history(period=timeFrame)
        dates = parse_dates(ticker_df)
        return dates

def stock_prices_combine(ticker, timeFrame='ytd', start=None, end=None):
    ticker = yfinance.Ticker(ticker)
    if start and end:
        ticker_df = ticker.history(start=start, end=end)
        prices = parse_prices(ticker_df)
        return prices
    else:
        ticker_df = ticker.history(period=timeFrame)
        prices = parse_prices(ticker_df)
        return prices






