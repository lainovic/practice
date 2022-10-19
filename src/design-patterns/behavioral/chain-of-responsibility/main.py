# Chain of Responsibility: Allows building a chain of objects to process a request.
#
# A `WebBrowser` class handles the request by processing it through the pipeline consisting of various handlers,
# effetively using the chain-of-responsibility pattern.
#
# Using the Big4 jargon:
#
# WebBrowser -> Sender
# Handler -> Handler
# SomeHandlerA -> Receiver
#


from abc import ABC, abstractmethod
from distutils.log import Log
from typing import Optional


class Request:
    def __init__(self, username, password, payload) -> None:
        self.username = username
        self.password = password
        self.payload = payload


class Response:
    pass


class Handler(ABC):

    next: 'Handler' = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self.next = handler
        return handler

    def handle(self, request: Request) -> Request:
        if self.next:
            return self.next.handle(request)
        return request


class Authenticator(Handler):
    def handle(self, request: Request) -> Request:
        print("Authenticating...")
        return super().handle(request)


class Decryptor(Handler):
    def handle(self, request: Request) -> Request:
        print("Decrypting...")
        return super().handle(request)


class Decompressor(Handler):
    def handle(self, request: Request) -> Request:
        print("Decompression failed, not continuing the chain.")
        return request
        # return super().handle(request)


class Logger(Handler):
    def handle(self, request: Request) -> Request:
        print("Logging...")
        return super().handle(request)


class WebBrowser:
    def __init__(self, handler: Optional[Handler] = None) -> None:
        self.handler = handler

    def serve(self, request: Request) -> Response:
        if self.handler:
            request = self.handler.handle(request)
        return self.process(request)

    def process(self, request: Request) -> Response:
        print(f"Finally processing {request}...")
        return Response()


if __name__ == "__main__":
    logger = Logger()
    decompressor = Decompressor()
    decryptor = Decryptor()
    authenticator = Authenticator()
    browser = WebBrowser(authenticator)
    authenticator.set_next(decryptor).set_next(decompressor).set_next(logger)

    browser.serve(Request(username="admin",
                          password="1234",
                          payload="GET /hello_there.html HTTP/2...")
                  )
