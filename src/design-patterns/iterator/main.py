# A `BrwoserHistory` class that has iterating over it supported by having providing the  `Iterator` interface,
# hence utilizing the Iterator Pattern.
#
# Using the Big4 jargon:
# BrowseHistory -> Iterable
# Iterator -> Iterator
#
# Same for `ProductCollection`

from abc import ABC, abstractmethod
from random import random
import sys
import uuid


class BrowseHistory:
    class Iterator(ABC):
        @abstractmethod
        def next(self) -> str:
            pass

        @abstractmethod
        def has_next(self) -> bool:
            pass

    class ListIterator(Iterator):
        def __init__(self, history) -> None:
            self.current_idx = 0
            self.history = history

        def next(self) -> str:
            res = self.history.urls[self.current_idx]
            self.current_idx += 1
            return res

        def has_next(self) -> bool:
            return self.current_idx < len(self.history.urls)

    def __init__(self) -> None:
        self.urls = []
        self.max_length = 10

    def push(self, url: str) -> None:
        if len(self.urls) < self.max_length:
            self.urls.append(url)
        else:
            raise RuntimeError(
                f"Error: history reached its capacity: {self.max_length}.")

    def pop(self) -> str:
        return self.urls.pop()

    def iterator(self) -> Iterator:
        if len(self.urls) == 0:
            return None
        return self.ListIterator(self)


class Product:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"""Product {{
    id= {self.id},
    name={self.name}
}}"""


class ProductCollection:
    class Iterator(ABC):
        @abstractmethod
        def next(self) -> Product:
            pass

        @abstractmethod
        def has_next(self) -> bool:
            pass

    class ListIterator(Iterator):
        def __init__(self, product_collection) -> None:
            self.current_idx = 0
            self.product_collection = product_collection

        def next(self):
            res = self.product_collection.products[self.current_idx]
            self.current_idx += 1
            return res

        def has_next(self):
            return self.current_idx < len(self.product_collection.products)

    def __init__(self) -> None:
        self.products = []

    def add(self, product):
        self.products.append(product)

    def iterator(self) -> ListIterator:
        return self.ListIterator(self)


if __name__ == "__main__":
    history = BrowseHistory()
    history.push("a")
    history.push("b")
    history.push("c")
    history.push("d")
    history.push("e")
    history.push("f")
    history.push("g")
    history.push("h")
    history.push("i")
    history.push("j")
    try:
        new_uri = "k"
        history.push(new_uri)
    except RuntimeError as e:
        print(f"Exception caught while pushing '{new_uri}'. ({e})")

    it = history.iterator()
    if not it:
        print("No iterator. History empty?")
        sys.exit(0)
    while it.has_next():
        print(it.next())

    print('------------------------------------------------------------------------')

    product_collection = ProductCollection()
    product_collection.add(Product(uuid.uuid4(), "foo"))
    product_collection.add(Product(uuid.uuid4(), "bar"))
    product_collection.add(Product(uuid.uuid4(), "baz"))
    it = product_collection.iterator()
    while it.has_next():
        print(f"{it.next()}\n")
