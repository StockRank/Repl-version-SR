import os

api_key = os.environ['stock_api_key']


def generateOverviewUrl(ticker):
  url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + api_key
  return url