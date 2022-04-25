"""
author: Nathan Lindley (nfl6fh)
Stocks assignment
"""

import pandas as pd


def main():
    filepath = 'apple_data.csv'
    dates = getDataFile(filepath)
    aapl = Stock('aapl', 'technology', dates)
    aapl.print_sector()
    aapl.get_rows_count()
    print(aapl.price_records)
    returns = [0]
    for i in range(1, len(aapl.prices)):
        today = float(aapl.prices['prices'][i])
        yest = float(aapl.prices['prices'][i-1])
        returns.append(((today-yest)/yest)*100)
    aapl.prices['returns'] = returns
    print(aapl.prices[0:5])


class Stock:
    def __init__(self, ticker, sector, prices):
        self.ticker = ticker
        self.prices = pd.DataFrame(prices, columns=('dates', 'prices'))
        self.price_records = 0
        self.sector = sector

    def print_sector(self):
        print('sector:', self.sector)

    def get_rows_count(self):
        self.price_records = len(self.prices)
        return self.price_records


def getDataFile(filepath):
    filehandle = open(filepath)

    titleRow = filehandle.readline()

    dataRows = filehandle.readlines()
    filehandle.close()

    listOfStocks = []
    for row in dataRows:
        date, price = row.split(",")
        listOfStocks.append((date, price.strip()))

    return listOfStocks


main()
