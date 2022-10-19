# State: Allows an object to behave differently depending on the state it is in.
#
# A `Canvas` class has its tools implemented via polymoprhism,
# effectively using the State pattern.
#
# :note: Or maybe this is more an example of a Strategy pattern? The states don't know about each other here.
#
# Using the Big4 jargon:
#
# Canvas -> Context
# Tool -> State
# SomeToolA -> ConcreteStateA
#
# Same for `DirectionService`.
#

from abc import ABC, abstractmethod
from enum import Enum


class Canvas:
    class ToolType(Enum):  # not used :(
        SELECTION = 1
        BRUSH = 2
        ERASER = 3

    class Tool(ABC):
        @abstractmethod
        def mouse_down(self):
            pass

        @abstractmethod
        def mouse_up(self):
            pass

    class SelectionTool(Tool):
        def mouse_down(self):
            print("SELECTION icon")

        def mouse_up(self):
            print("Draw a dashed rectangle.")

    class BrushTool(Tool):
        def mouse_down(self):
            print("BRUSH icon")

        def mouse_up(self):
            print("Draw a line.")

    class EraserTool(Tool):
        def mouse_down(self):
            print("ERASER icon")

        def mouse_up(self):
            print("Erase something.")

    def __init__(self) -> None:
        self.current_tool = None

    def mouse_down(self):
        if not self.current_tool:
            raise RuntimeError("Error: no tool selected.")
        self.current_tool.mouse_down()

    def mouse_up(self):
        if not self.current_tool:
            raise RuntimeError("Error: no tool selected.")
        self.current_tool.mouse_up()


class DirectionService:
    class TravelMode(Enum):  # not used :(
        DRIVING = 0
        BICYCLING = 1
        TRANSIT = 2
        WALKING = 4

    class TravelModeBase(ABC):
        @abstractmethod
        def get_eta(self):
            pass

        @abstractmethod
        def get_direction(self):
            pass

    class DrivingMode(TravelModeBase):
        def get_eta(self):
            print("Calculating ETA (Driving)")
            return 1

        def get_direction(self):
            print("Calculating Direction (Driving)")
            return 1

    class BicycleMode(TravelModeBase):
        def get_eta(self):
            print("Calculating ETA (Bicycle)")
            return 2

        def get_direction(self):
            print("Calculating Direction (Bicycle)")
            return 2

    class TransitMode(TravelModeBase):
        def get_eta(self):
            print("Calculating ETA (Transit)")
            return 3

        def get_direction(self):
            print("Calculating Direction (Transit)")
            return 3

    class WalkingMode(TravelModeBase):
        def get_eta(self):
            print("Calculating ETA (Walking)")
            return 4

        def get_direction(self):
            print("Calculating Direction (Walking)")
            return 4

    def __init__(self) -> None:
        self.current_mode = self.WalkingMode()
        self.current_mode_enum = self.TravelMode.WALKING

    def get_eta(self):
        return self.current_mode.get_eta()

    def get_direction(self):
        return self.current_mode.get_direction()


if __name__ == "__main__":
    canvas = Canvas()

    try:
        canvas.mouse_down()
    except RuntimeError as err:
        print(err)

    canvas.current_tool = Canvas.BrushTool()
    canvas.mouse_down()
    canvas.mouse_up()

    canvas.current_tool = Canvas.SelectionTool()
    canvas.mouse_down()
    canvas.mouse_up()

    canvas.current_tool = Canvas.EraserTool()
    canvas.mouse_down()
    canvas.mouse_up()

    print('------------------------------------------------------------------------')

    svc = DirectionService()
    svc.get_eta()
    svc.get_direction()

    svc.current_mode = DirectionService.DrivingMode()
    svc.get_eta()
    svc.get_direction()

    svc.current_mode = DirectionService.BicycleMode()
    svc.get_eta()
    svc.get_direction()

    svc.current_mode = DirectionService.TransitMode()
    svc.get_eta()
    svc.get_direction()
