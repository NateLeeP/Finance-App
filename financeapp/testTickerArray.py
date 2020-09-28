from financeapp import betaFunctions as bf
from financeapp import dateLookUp as dl
import datetime

testArray = [{'Ticker':'TSLA', 'Shares':20}, {'Ticker':'F', 'Shares':50}, {'Ticker':'FB', 'Shares':30}, {'Ticker':'SPY', 'Shares':50}, {'Ticker':'AMZN', 'Shares':10}]

# Expected Market Return is in form of percentage
expectedMarketReturn = -56


bf.getMultipleBeta(testArray)
bf.getMultiplePrice(testArray)
bf.getPortfolioPercentage(testArray, bf.getPortfolioValue(testArray))
bf.getCAPM(testArray, expectedMarketReturn)
bf.getPortfolioBeta(testArray)

#(dl.price_array[:5])

totalExpectedReturn = float("{:.2f}".format(bf.portfolioExpectedReturn(testArray)))
newTotalPortfolioValue = bf.getPortfolioValue(testArray) * (1 + (totalExpectedReturn/100))
beginTotalPortfolioValue = bf.getPortfolioValue(testArray)
requiredReturn = bf.calculateRequiredReturn(beginTotalPortfolioValue, newTotalPortfolioValue)
daysToRecover = dl.daysLookUp(requiredReturn, bf.getPortfolioBeta(testArray))

#print(bf.getPortfolioBeta(testArray))
#print(dl.price_array[:5])