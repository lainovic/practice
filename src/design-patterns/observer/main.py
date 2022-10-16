# Observer: Allows an object notify other objects when its state changes.
#
# A `DataSource` class has its changes broadcasted to other classes
# that get notified and react appropriately.
#
# Using the Big4 jargon:
#
# DataSource -> Observable
# Chart -> Observer
#
# Same for `Stock`.
#

from abc import ABC, abstractmethod
from re import S
from tkinter import N
from tkinter.messagebox import NO
from typing import List


class Observable():
    class Observer(ABC):
        @abstractmethod
        def update(self):
            pass

    def __init__(self) -> None:
        self.observers: List[Observable.Observer] = []

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        for obs in self.observers:
            obs.update()


class DataSource(Observable):

    def __init__(self, value=0) -> None:
        super().__init__()
        self.val = value

    def set_value(self, value):
        self.val = value
        self.notify()


class Chart(Observable.Observer):
    def __init__(self, src) -> None:
        self.src = src

    def update(self):
        print(f"{type(self).__name__} updated with {src.val}!")


class Spreadsheet(Observable.Observer):
    def __init__(self, src) -> None:
        self.src = src

    def update(self):
        print(f"{type(self).__name__} updated with value {src.val}!")


class Stock(Observable):
    def __init__(self, symbol, price) -> None:
        super().__init__()
        self.symbol = symbol
        self.price = price

    def set_price(self, new_price) -> None:
        if self.price == new_price:
            return
        self.price = new_price
        self.notify()

    def __str__(self) -> str:
        return f"""Stock{{
symbol={self.symbol},
price={self.price}
}}"""


class StatusBar(Observable.Observer):
    def __init__(self) -> None:
        super().__init__()
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)
        stock.attach(self)

    def show(self):
        print("Stocks in the status bar:")
        for stock in self.stocks:
            print(stock)

    def update(self):
        print(
            f"[{self.__class__.__name__}] Prices changed! Refreshing the status bar...")
        self.show()


class StockListView(Observable.Observer):
    def __init__(self) -> None:
        super().__init__()
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)
        stock.attach(self)

    def show(self):
        print("Stocks in the stock-view:")
        for stock in self.stocks:
            print(stock)

    def update(self):
        print(
            f"[{self.__class__.__name__}] Prices changed! Refreshing the stock list view...")
        self.show()


if __name__ == "__main__":
    src = DataSource()
    chart = Chart(src)
    sheet1 = Spreadsheet(src)
    sheet2 = Spreadsheet(src)
    src.attach(sheet1)
    src.attach(chart)
    src.attach(sheet2)
    src.set_value(42)

    print('------------------------------------------------------------------------')

    status_bar = StatusBar()
    stock_list = StockListView()
    aapl_stock = Stock("AAPL", 100)
    status_bar.add_stock(aapl_stock)
    stock_list.add_stock(aapl_stock)
    msft_stock = Stock("MSFT", 80)
    stock_list.add_stock(msft_stock)
    status_bar.show()
    stock_list.show()
    new_price = 150
    print(f"... AAPL stock price will cnange to ${new_price}...")
    aapl_stock.set_price(new_price)
    new_price = 92
    print(f"... MSFT stock price will cnange to ${new_price}...")
    msft_stock.set_price(new_price)
