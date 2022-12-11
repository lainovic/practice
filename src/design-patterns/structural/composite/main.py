"""
Composite Pattern lets you compose objects into tree structures,
and then treat these structures as if they were the same objects themselves.

:
```mermaid
classDiagram
    class Component {
        +operation()
    }
    Component <|-- Leaf
    Component <|-- Composite
    Component "0..*" --* Composite
```
"""


from abc import ABC, abstractmethod
from typing import List


def get_id(obj):
    return hex(id(obj) % pow(16, 4))


class Component(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Shape(Component):
    def render(self):
        print(f"Shape {get_id(self)} rendered!")

    def move(self):
        print(f"Shape {get_id(self)} moved!")


class Group(Component):
    def __init__(self) -> None:
        self.components: List[Component] = []

    def add(self, component: Component):
        self.components.append(component)

    def render(self):
        for componenet in self.components:
            componenet.render()
        print(f"Group {get_id(self)} rendered!")

    def move(self):
        for componenet in self.components:
            componenet.move()
        print(f"Group {get_id(self)} moved!")


if __name__ == "__main__":
    group_1 = Group()  # squares
    group_1.add(Shape())
    group_1.add(Shape())

    group_2 = Group()  # circles
    group_2.add(Shape())
    group_2.add(Shape())

    group = Group()  # container
    group.add(group_1)
    group.add(group_2)

    print("Render:")
    group.render()
    print("Move:")
    group.move()

    print("------------------------------------------------------------------------")
