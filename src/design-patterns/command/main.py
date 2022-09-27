# A `VideoEditor` class that has its closing behavior customized via before/after hooks,
# effectively using the Template pattern.
#
# Using the Big4 jargon:
# Window -> Context
# Compressor -> Strategy
# SomeCompressorA -> ConcreteStrategyA


from abc import ABC, abstractmethod
from cmath import log
from tkinter import *


class VideoEditor:
    def __init__(self) -> None:
        self.contrast = 0.5
        self.text = ""

    def __str__(self) -> str:
        return f"""VideoEditor {{
contrast: {self.contrast},
text: {self.text}
}}"""


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class UndoableCommand(Command):
    @abstractmethod
    def undo(self):
        pass


class History:
    def __init__(self) -> None:
        self.cmds = []

    def push(self, cmd: UndoableCommand) -> None:
        self.cmds.append(cmd)

    def pop(self) -> UndoableCommand:
        return self.cmds.pop()

    def empty(self):
        return len(self.cmds) == 0


class UndoCommand():
    def __init__(self, history: History) -> None:
        self.history = history

    def execute(self) -> None:
        if not self.history.empty():
            self.history.pop().undo()


class CompositeCommand(Command):
    def __init__(self) -> None:
        self.cmds = []

    def add(self, cmd: Command):
        self.cmds.append(cmd)

    def execute(self):
        for cmd in self.cmds:
            cmd.execute()


class AddTextCommand(UndoableCommand):
    def __init__(self, editor: VideoEditor, history: History, text: str) -> None:
        self.editor = editor
        self.history = history
        self.text = text
        self.prev_text = ""

    def execute(self):
        self.prev_text = self.editor.text
        self.editor.text = self.text
        self.history.push(self)
        print(self.editor)

    def undo(self):
        self.editor.text = self.prev_text


class ChangeContrastCommand(Command):
    def __init__(self, editor, contrast) -> None:
        self.editor = editor
        self.contrast = contrast

    def execute(self):
        self.editor.contrast = self.contrast
        print(self.editor)


if __name__ == "__main__":
    editor = VideoEditor()
    editor.text = "lorem ipsum"
    print(editor)

    change_contrast_cmd = ChangeContrastCommand(editor, 1)

    history = History()
    add_text_cmd = AddTextCommand(editor, history, "foo bar")

    undo_cmd = UndoCommand(history)

    all_cmd = CompositeCommand()
    all_cmd.add(change_contrast_cmd)
    all_cmd.add(add_text_cmd)
    all_cmd.add(undo_cmd)

    window = Tk()
    window.title("Command Pattern in Action")
    window.geometry('350x200')

    def on_change_contrast_clicked():
        change_contrast_cmd.execute()

    change_contrast_btn = Button(
        window, text="Change contrast to 1", command=on_change_contrast_clicked)
    change_contrast_btn.grid(sticky="W", column=1, row=0)

    def on_add_text_clicked():
        add_text_cmd.execute()

    add_text_btn = Button(
        window, text="Change text to 'foo bar'", command=on_add_text_clicked)
    add_text_btn.grid(sticky="W", column=1, row=1)

    def on_undo_clicked():
        undo_cmd.execute()
        print(editor)

    undo_btn = Button(window, text="Undo",
                      command=on_undo_clicked)
    undo_btn.grid(sticky="W", column=1, row=2)

    def on_do_all_clicked():
        all_cmd.execute()
        print(editor)

    do_all_btn = Button(window, text="Do all the above",
                        command=on_do_all_clicked)
    do_all_btn.grid(sticky="W", column=1, row=3)

    window.mainloop()
