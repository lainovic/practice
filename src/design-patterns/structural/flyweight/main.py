"""
Flyweight lets you fit more objects into RAM by sharing common parts of state between multiple objects,
instead of keeping all of the data in each object.
Common parts are stored in a cache or some pool of objects, ready to be reused.

GoF diagram:
```mermaid
classDiagram
    class FlyweightFactory {
        +get(): Flyweight
        flyweights: map< hash, Flyweight >
    }
    Flyweight --*"0..*" FlyweightFactory
    SomeObject --> Flyweight
    SomeObject --*"0..*" SomeObjectConsumer
    FlyweightFactory <.. SomeObjectConsumer
```
"""

from enum import Enum


class PointIcon:
    class Type(Enum):
        CAFE = 1,
        HOSPITAL = 2

    def __init__(self, type, icon_path) -> None:
        self.type = type
        self.icon_path = icon_path


class PointIconFactory:
    icons = {}

    @classmethod
    def get(cls, type) -> PointIcon:
        log_msg = f"[LOG][DEBUG] Icon {type} "
        if type not in cls.icons:
            log_msg += "instantiated."
            cls.icons[type] = PointIcon(type, None)
        else:
            log_msg += "reused."
        print(log_msg)
        return cls.icons[type]


class Point:
    class Type(Enum):
        CAFE = 1,
        HOSPITAL = 2

    def __init__(self, x, y, icon) -> None:
        self.x = x
        self.y = y
        self.icon = icon

    def draw(self):
        print(
            f"[LOG][INFO] {self.icon.type} point at ({self.x}, {self.y}) drawn.")


class PointService:
    def __init__(self, factory) -> None:
        self.points = []
        p1 = Point(1, 2, factory.get(PointIcon.Type.CAFE))
        p2 = Point(-1, 1, factory.get(PointIcon.Type.CAFE))
        p3 = Point(0, 3, factory.get(PointIcon.Type.CAFE))
        p4 = Point(0, 3, factory.get(
            PointIcon.Type.HOSPITAL))
        p5 = Point(1, -5, factory.get(
            PointIcon.Type.HOSPITAL))
        self.points.extend([p1, p2, p3, p4, p5])


class CellContext:
    def __init__(self, font_family, font_size, is_bold) -> None:
        self.font_family = font_family
        self.font_size = font_size
        self.is_bold = is_bold

    class Factory:
        def __init__(self) -> None:
            self.contexts = {}

        def get(self, font_family="sans serif", font_size=18, is_bold=False):
            log_msg = f"[LOG][DEBUG] Context [{font_family}][{font_size}][{is_bold}] "
            h = hash(font_family) + hash(font_size) + hash(is_bold)
            if h not in self.contexts:
                self.contexts[h] = CellContext(
                    font_family, font_size, is_bold)
                log_msg += "created."
            else:
                log_msg += "reused."
            print(log_msg)
            return self.contexts[h]


class Cell:
    def __init__(self, row, col, content, cell_context) -> None:
        self.row = row
        self.col = col
        self.content = content
        self.cell_context = cell_context


class Spreadsheet:
    def __init__(self, context_factory) -> None:
        self.context_factory = context_factory
        self.cells = []

    def _ensure_cell_exists(self, row, col):
        while row >= len(self.cells):
            self.cells.append([])
        while col >= len(self.cells[row]):
            self.cells[row].append(None)

    def _cell_exists(self, row, col):
        return row in range(len(self.cells)) and col in range(len(self.cells[row]))

    def set_content(self, row, col, content):
        self._ensure_cell_exists(row, col)
        self.cells[row][col] = Cell(
            row, col, content, cell_context=self.context_factory.get())

    def set_font_family(self, row, col, font_family):
        if not self._cell_exists(row, col):
            return
        cell = self.cells[row][col]
        ctx = cell.cell_context
        cell.cell_context = self.context_factory.get(
            font_family, ctx.font_size, ctx.is_bold)


if __name__ == "__main__":
    svc = PointService(PointIconFactory)
    for p in svc.points:
        p.draw()

    print("------------------------------------------------------------------------")

    sheet = Spreadsheet(CellContext.Factory())
    sheet.set_content(0, 0, "foo")
    sheet.set_content(0, 1, "bar")
    sheet.set_content(1, 0, "baz")
    sheet.set_font_family(1, 0, "Arial")
    sheet.set_font_family(1, 0, "Arial")
    sheet.set_font_family(1, 1, "Arial")
