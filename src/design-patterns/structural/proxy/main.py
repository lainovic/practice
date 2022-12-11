"""
Proxy lets you provide a substitute or placeholder for another object.
A proxy controls access to the original object, allowing you to perform
something either before or after the request gets through to the original
object; the Proxy pattern suggests that we can create a new proxy class with
the same interface as an original object.
Frequently used for stuff like lazy initialization.

Real-World Analogy:
A credit card is a proxy for a bank account, which is a proxy for a bundle of cash.
Both implement the same interface: they can be used for making a payment.
A consumer feels great because there is no need to carry loads of cash around.
A shop owner is also happy since the income from a transaction gets added electronically
to their bank account without the risk of losing the deposit or getting robbed on the way to the bank.

For more: https://refactoring.guru/design-patterns/proxy

```mermaid
classDiagram
Client --> Subject
class Subject {
    <<abstract>>
    +request()
}
RealSubject --|> Subject
ProxySubject --|> Subject
ProxySubject o-- RealSubject : contains
```
"""


from time import sleep
from typing import Dict, Optional, Protocol
from lorem import get_sentence


class Ebook(Protocol):
    fileName: str

    def show(self) -> str:
        ...


class EbookProxy(Ebook):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
        self.ebook = None

    def show(self) -> str:
        if self.ebook is None:
            self.ebook = RealEbook(self.filename)
        return self.ebook.show()


class RealEbook(Ebook):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
        self.contents = ""
        self.load()

    def show(self) -> str:
        return self.contents

    def load(self):
        print(f"Loading the ebook '{self.filename}'...")
        sleep(1)
        self.contents = get_sentence(count=1, comma=(0, 2), word_range=(4, 8))


class Library:
    def __init__(self) -> None:
        self.books: Dict[str, Ebook] = {}

    def add(self, book: Ebook):
        self.books[book.filename] = book

    def open_book(self, filename) -> Optional[str]:
        return self.books[filename].show() if filename in self.books else None


if __name__ == "__main__":
    lib = Library()
    filenames = ["a", "b", "c"]
    for filename in filenames:
        lib.add(EbookProxy(filename))
    print(f"Book '{filenames[0]}' contents: {lib.open_book(filenames[0])}")
