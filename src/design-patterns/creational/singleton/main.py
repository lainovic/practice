"""
The Singleton Pattern is useful when exactly one object is needed to coordinate actions across a system.

GoF diagram:
```mermaid
classDiagram
class Singleton {
    -Singleton instance
    -Singleton()
    +getInstance() Singleton
}
```
"""


import stat


class Logger():
    _instance = None

    def __init__(self, filename) -> None:
        self.filename = filename

    def log(self, message):
        print(f"[LOG] \"{message}\" saved to {self.filename}")

    @staticmethod
    def get_instance() -> "Logger":
        if __class__._instance:
            return __class__._instance
        else:
            __class__._instance = Logger("default_filename.log")
            return __class__._instance


if __name__ == "__main__":
    Logger.get_instance().log("blabla")
    Logger.get_instance().log("foobar")
