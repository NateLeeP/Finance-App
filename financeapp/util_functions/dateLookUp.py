import csv
import datetime
import copy
price_array = []
with open('financeapp/sp500returns.csv', mode='r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      line_count += 1
      continue
    else:
      price_object = {}
      price_object['Date'] = row[0]
      price_object['Price'] = float(row[1])
      price_array.append(price_object.copy())
      line_count += 1
base_price = price_array[0]['Price']
for i in range(len(price_array)):
  if i == 0:
    price_array[i]['Change'] = 0.0
  else:
    price_array[i]['Change'] = ((price_array[i]['Price'] - base_price) / base_price) * 100


def convertToDate(dateString):
  year = int(dateString.split('-')[0])
  month = int(dateString.split('-')[1].lstrip('0'))
  day = int(dateString.split('-')[2].lstrip('0'))
  return datetime.date(year, month, day)

def adjustPriceArrayFunc(beta):
  adjustedPriceArray = price_array[:]
  for i in range(len(adjustedPriceArray)):
    adjustedPriceArray[i]['Change'] *= beta

  return adjustedPriceArray


def daysLookUp(required_return, portfolio_beta, isFinancialCrisis):
  date = ''
  if isFinancialCrisis:

    adjustPriceArray= copy.deepcopy(price_array)
    # 'deepcopy' ensures dictionairies in list are copied. Need to copy, python passes everything by reference.
    for i in range(len(adjustPriceArray)):
     adjustPriceArray[i]['Change'] *= portfolio_beta
    for i in range(len(adjustPriceArray)):
      if adjustPriceArray[i]['Change'] > required_return:
        date = convertToDate(adjustPriceArray[i]['Date'])
        break
    del adjustPriceArray
    return (date - datetime.date(2009, 3, 8)).days
  # Work in progress. Attempting to add 2020 crash as part of Risk analysis.
  else:
    adjustPriceArray = filter(lambda x: x['Date'] >= '2020-03-23', price_array)
    for i in range(len(adjustPriceArray)):
     adjustPriceArray[i]['Change'] *= portfolio_beta
    for i in range(len(adjustPriceArray)):
      if adjustPriceArray[i]['Change'] > required_return:
        date = convertToDate(adjustPriceArray[i]['Date'])
        break
    del adjustPriceArray
    if date == '':
      date = 'Not recovered yet!'
      return date
    else:
      return (date - datetime.date(2020, 3, 20)).days

def recoveryDate(days):
  # Accepts recovery days and returns date of recovery (as string)
  if isinstance(days, int) is False:
    return days
  else:
    return (datetime.date.today() + datetime.timedelta(days=days)).strftime("%B %d, %Y")

def test():
  print(price_array[:5])