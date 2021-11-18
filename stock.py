class stock():
  def __init__(self, ticker, description, exchange, currency, eps, peRatio):
    self.ticker = ticker
    self.description = description
    self.exchange = exchange
    self.currency = currency
    self.eps = eps
    self.peRatio = peRatio

  def getTicker(self):
    return self.ticker
  def getDescription(self):
    return self.description
  def getExchange(self):
    return self.exchange
  def getCurrency(self):
    return self.currency
  def getEPS(self):
    return self.eps
  def getPERatio(self):
    return self.peRatio