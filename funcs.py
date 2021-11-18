import os
import requests
from api_fetcher import generateOverviewUrl


def retrieveFunction(ticker):
  r = requests.get(generateOverviewUrl(ticker))
  data = r.json()
  return data['MarketCapitalization'], data['EBITDA'], data['PERatio'], data['DividendYield'], data['EPS']