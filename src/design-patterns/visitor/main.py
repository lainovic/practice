# A `HTMLDocument` class, having a fixed set of `HTMLNode` implementations,
# adds new functionality to these nodes without changing their classes,
# effectively using the Visitor pattern.
#
# Using the Big4 jargon:
# HTMLNode -> Element
# HeadingNode -> ConcreteElementA
# Operation -> Visitor
# HighlightOperation -> ConcreteVisitorA
#
# Same for `WavFile`.
#

from abc import ABC, abstractmethod
from typing import List
from wave import WAVE_FORMAT_PCM, Wave_read

from regex import F


class HTMLNode(ABC):
    @abstractmethod
    def execute(self, op: "Operation"):
        pass


class HeadingNode(HTMLNode):
    def execute(self, op: "Operation"):
        op.apply_to_heading(self)


class AnchorNode(HTMLNode):
    def execute(self, op: "Operation"):
        op.apply_to_anchor(self)


class Operation(ABC):
    @abstractmethod
    def apply_to_heading(self, node: "HeadingNode") -> None:
        pass

    @abstractmethod
    def apply_to_anchor(self, node: "AnchorNode") -> None:
        pass


class HTMLDocument:
    def __init__(self) -> None:
        self.nodes: List[HTMLNode] = []

    def add(self, node: "HTMLNode"):
        self.nodes.append(node)

    def execute(self, op):
        for node in self.nodes:
            node.execute(op)


class HighlightOperation(Operation):
    def apply_to_heading(self, node: "HeadingNode") -> None:
        print(f"Highlighting heading at {node}")

    def apply_to_anchor(self, node: "AnchorNode") -> None:
        print(f"Highlighting anchor at {node}")


class PlainttextOperation(Operation):
    def apply_to_heading(self, node: "HeadingNode") -> None:
        print(f"Extracting plain text from heading at {node}")

    def apply_to_anchor(self, node: "AnchorNode") -> None:
        print(f"Extracting plain text from anchor at {node}")


class AudioFilter(ABC):
    @abstractmethod
    def apply_to_format_segment(self, format_segment: "FormatSegment"):
        pass

    @abstractmethod
    def apply_to_fact_segment(self, fact_segment: "FactSegment"):
        pass


class NormalizeFilter(AudioFilter):
    def apply_to_format_segment(self, format_segment: "FormatSegment"):
        print(f"Normalize the {format_segment}.")

    def apply_to_fact_segment(self, fact_segment: "FactSegment"):
        print(f"Normalize the {fact_segment}")


class BrandNewFilter(AudioFilter):
    def apply_to_format_segment(self, format_segment: "FormatSegment"):
        print(f"Brand new filtering the {format_segment}.")

    def apply_to_fact_segment(self, fact_segment: "FactSegment"):
        print(f"Brand new filtering the {fact_segment}")


class Segment(ABC):
    @abstractmethod
    def apply_filter(self, filter: AudioFilter):
        pass


class FormatSegment(Segment):
    def apply_filter(self, filter: AudioFilter):
        filter.apply_to_format_segment(self)


class FactSegment(Segment):
    def apply_filter(self, filter: AudioFilter):
        filter.apply_to_fact_segment(self)


class WavFile:
    def __init__(self) -> None:
        self.segments: List[Segment] = []

    def read(self, wav_file_path: str) -> None:
        print("Reading the WAV file.")

        self.segments.append(FactSegment())
        self.segments.append(FactSegment())
        self.segments.append(FormatSegment())
        self.segments.append(FormatSegment())
        self.segments.append(FormatSegment())

    def execute_filter(self, filter: AudioFilter):
        for segment in self.segments:
            segment.apply_filter(filter)


if __name__ == "__main__":
    document = HTMLDocument()
    document.add(HeadingNode())
    document.add(AnchorNode())
    document.execute(HighlightOperation())
    document.execute(PlainttextOperation())

    print('------------------------------------------------------------------------')

    wav_file = WavFile()
    wav_file.read("https://foo.bar/xyz")

    wav_file.execute_filter(NormalizeFilter())
    wav_file.execute_filter(BrandNewFilter())
