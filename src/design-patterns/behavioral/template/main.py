# Allows defining a template (skeleton) for an operation.
# Specific steps will then be implemented in subclasses.
#
# A `Window` class that has its closing behavior customized via before/after hooks,
# effectively using the Template pattern.
#
# Using the Big4 jargon:
#
# Window -> AbstractClass
# XWindow -> ConcreteClass
#
# Same for `Task`.
#

from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager


class DefaultAuditTrail:
    def record(self):
        print("Audit recorded.")


class Task(ABC):
    def __init__(self, audit_trail=DefaultAuditTrail()) -> None:
        self.audit_trail = audit_trail

    def execute(self):
        self.audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass


class TransferMoney(Task):
    def _do_execute(self):
        print("Money transferred.")


class GenerateReport(Task):
    def _do_execute(self):
        print("Report generated.")


class Window:
    def __init__(self) -> None:
        pass

    def _on_closing(self):
        print("Default empty on closing action.")

    def _on_closed(self):
        print("Default empty on closed action.")

    def close(self):
        self._on_closing()
        print("Removing the window from the screen.")
        self._on_closed()


class XWindow(Window):
    def _on_closed(self):
        print("X on closed action.")


if __name__ == "__main__":
    xwin = XWindow()
    xwin.close()

    print("------------------------------------------------------------------------")

    task = TransferMoney()
    task.execute()

    task = GenerateReport()
    task.execute()
