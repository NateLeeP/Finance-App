import csv
import datetime
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

def adjustPriceArray(beta):
  for i in range(len(price_array)):
    price_array[i]['Change'] *= beta

  return price_array


def daysLookUp(required_return, beta):
  date = ''
  price_array = adjustPriceArray(beta)
  for i in range(len(price_array)):
    if price_array[i]['Change'] > required_return:
      date = convertToDate(price_array[i]['Date'])
      break
  return (date - datetime.date(2009, 3, 8)).days

