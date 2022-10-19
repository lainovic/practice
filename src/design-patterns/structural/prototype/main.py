"""
Prototype is a design pattern used to spawn (polymorphic) objects basing on some existing instance.
prototype is used when there could be any possible implementation of some interface,
and you just want to obtain a new object of exactly the same implementation,
without resorting to some weird casting and checking methods.

GoF diagram:
```mermaid
classDiagram
Client..>Prototype
Prototype<|--ConcretePrototype
Prototype: +clone()
ConcretePrototype: +clone()
```
"""

from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def clone(self) -> "Component":
        pass

    @abstractmethod
    def whoami(self):
        pass


class Circle(Component):

    def __init__(self) -> None:
        super().__init__()
        self.radius = 5

    def clone(self) -> "Component":
        new_circle = Circle()
        new_circle.radius = self.radius
        return new_circle

    def whoami(self):
        return f"I am a Circle with radius {self.radius} at {hex(id(self))}"


def make_component() -> "Component":
    return Circle()


if __name__ == "__main__":
    some_component = make_component()
    print(some_component.whoami())
    new_clone = some_component.clone()
    print(f"A clone: {new_clone.whoami()}")
