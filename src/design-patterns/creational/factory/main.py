"""
Factory Method provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

:
```mermaid
classDiagram
    class Event
    class Scheduler{
        +schedule(event: Event)
        #createCalendar()
    }
    class Calendar{
        +addEvent()
    }
    Calendar <|-- GregorianCalendar
    Calendar <|-- ArabianCalendar
    Scheduler o-- GregorianCalendar
    Scheduler <|-- ArabianScheduler
    ArabianScheduler o-- ArabianCalendar
```
"""

from abc import ABC, abstractmethod
from datetime import date


class Calendar(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add_event(self) -> None:
        pass


class Event:
    def __init__(self) -> None:
        pass


class GregorianCalendar:
    def __init__(self) -> None:
        pass

    def add_event(self, event) -> None:
        print(f"Event {event} added on {date.today()} in Gregorian calendar.")


class ArabianCalendar:
    def __init__(self) -> None:
        pass

    def add_event(self, event) -> None:
        print(f"Event {event} added on {date.today()} in Arabian calendar.")


class Scheduler:
    def __init__(self) -> None:
        self.create_calendar()

    def create_calendar(self):
        self.calendar = GregorianCalendar()

    def schedule(self, event):
        self.calendar.add_event(event)


class ArabianScheduler(Scheduler):
    def create_calendar(self):
        self.calendar = ArabianCalendar()


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.schedule(Event())

    scheduler = ArabianScheduler()
    scheduler.schedule(Event())
