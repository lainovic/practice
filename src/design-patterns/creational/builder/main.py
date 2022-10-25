"""
Builder is a design pattern that lets you:
1. Construct complex objects step by step.
2. Produce different types and representations of an object using the same construction code.

```mermaid
classDiagram
    class Builder {
        +add_elementA()
        +add_elementB()
    }
    Builder <|-- ConcreteBuilder1
    Builder <|-- ConcreteBuilder2

    Component ..> Builder
    Client --> ConcreteBuilder1
    Client --> ConcreteBuilder2
    Client --> Component
```
"""


from abc import ABC, abstractmethod
from telnetlib import TELNET_PORT
from typing import List


class Element:
    pass


class TextElement(Element):
    def __init__(self, text) -> None:
        super().__init__()
        self.text = text


class ImageElement(Element):
    def __init__(self, img_path) -> None:
        super().__init__()
        self.img_path = img_path


class DocumentBuilder(ABC):
    @abstractmethod
    def add_text_element(self, e: TextElement):
        pass

    def add_image_element(self, e: ImageElement):
        pass


class HTML:
    class Builder(DocumentBuilder):
        def __init__(self) -> None:
            super().__init__()
            self.document = []

        def add_text_element(self, e: TextElement):
            self.document.append(f"<p>{e.text}</p>")

        def add_image_element(self, e: ImageElement):
            self.document.append(f"<img href=\"{e.img_path}\"></img>")

        def build(self) -> "HTML":
            return "\n".join(self.document)


class Text:
    class Builder(DocumentBuilder):
        def __init__(self) -> None:
            super().__init__()
            self.words = []

        def add_text_element(self, e: TextElement):
            self.words.append(f"- {e.text}")

        def add_image_element(self, _: ImageElement):
            pass

        def build(self) -> "Text":
            return "\n".join(self.words)


class Document:
    def __init__(self) -> None:
        self.elements: List[Element] = []

    def add(self, e: Element):
        self.elements.append(e)

    def export(self, builder: DocumentBuilder):
        for e in self.elements:
            if isinstance(e, TextElement):
                builder.add_text_element(e)
            elif isinstance(e, ImageElement):
                builder.add_image_element(e)


if __name__ == "__main__":
    doc = Document()

    doc.add(TextElement("Hello there!"))
    doc.add(ImageElement("/lain/home/Downloads/obiwan.jpg"))
    doc.add(TextElement("General Kenobi!"))
    doc.add(ImageElement("/lain/home/Downloads/generalgrievous.jpg"))

    builder = HTML.Builder()
    doc.export(builder)
    html = builder.build()
    print(f"html:\n{html}")

    builder = Text.Builder()
    doc.export(builder)
    txt = builder.build()
    print(f"text:\n{txt}")
