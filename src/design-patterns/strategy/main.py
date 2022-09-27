# A `ChatClient` class that has its compression algorithm offloaded to the other class,
# effectively using the Strategy pattern.
#
# Using the Big4 jargon:
# ChatClient -> Context
# Compressor -> Strategy
# SomeCompressorA -> ConcreteStrategyA
#
# Same for `ImageStorage`

from abc import ABC, abstractmethod
from re import S


class Compressor(ABC):
    @abstractmethod
    def compress(self, filename):
        pass


class Filter(ABC):
    @abstractmethod
    def filter(self):
        pass


class JPEGCompressor(Compressor):
    def compress(self, filename):
        print(f"{filename} compressed using JPEG.")


class PNGCompressor(Compressor):
    def compress(self, filename):
        print(f"{filename} compressed using PNG.")


class BWFilter(Filter):
    def filter(self, filename):
        print(f"B&W filter applied to {filename}.")


class HighContrastFilter(Filter):
    def filter(self, filename):
        print(f"High-contrast filter applied to {filename}.")


class EncryptionStrategy(ABC):
    @abstractmethod
    def encrypt(self, msg: str) -> str:
        pass


class DES(EncryptionStrategy):
    def encrypt(self, msg: str) -> str:
        print(f"Encrypting \"{msg}\" with DES.")
        return msg


class AES(EncryptionStrategy):
    def encrypt(self, msg: str) -> str:
        print(f"Encrypting \"{msg}\" with AES.")
        return msg


class ChatClient:
    def __init__(self, encryption_strategy=None) -> None:
        self.encryption_strategy = encryption_strategy

    def send(self, msg):
        if self.encryption_strategy:
            msg = self.encryption_strategy.encrypt(msg)
        print(f"\"{msg}\" sent.")


class ImageStorage():
    def __init__(self, compressor, filter) -> None:
        self.compressor = compressor
        self.filter = filter

    def store(self, filename, compressor=None, filter=None):
        if compressor:
            compressor.compress(filename)
        else:
            self.compressor.compress(filename)
        if filter:
            filter.filter(filename)
        else:
            self.filter.filter(filename)


if __name__ == "__main__":
    img_storage = ImageStorage(PNGCompressor(), HighContrastFilter())
    img_storage.store("kenobi.png")
    img_storage.store("kenobi.jpg", JPEGCompressor(), BWFilter())

    print('------------------------------------------------------------------------')

    chat_client = ChatClient()
    chat_client.send("Hello there!")

    chat_client = ChatClient(AES())
    chat_client.send("Hello there!")
