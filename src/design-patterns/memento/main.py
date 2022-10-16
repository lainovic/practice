# Memento: Allows restoring an object to a previous state.
#
# An `Editor` class  has its undo/redo functionaliy decoupled
# via History class and Snapshot class that is used within both.
#
# Using the Big4 jargon:
#
# Editor -> Originator
# Snapshot -> Memento
# History -> Caretaker
#

from copy import copy


class Editor:
    def __init__(self) -> None:
        self.default_state = Editor.Snapshot(
            content="", font_name="Sans Serif", font_size=16)
        self.current_snapshot = copy(self.default_state)
        self.history = Editor.History()

    def __str__(self) -> str:
        return f"Editor {{" \
               f"content={self.current_snapshot.content if self.current_snapshot.content else None}, " \
               f"font_name={self.current_snapshot.font_name}, " \
               f"font_size={self.current_snapshot.font_size}}}"

    def set_content(self, content):
        self._save()
        self.current_snapshot.content = content

    def get_content(self):
        return self.current_snapshot.content

    def set_font_name(self, font_name):
        self._save()
        self.current_snapshot.font_name = font_name

    def get_font_name(self):
        return self.current_snapshot.font_name

    def set_font_size(self, font_size):
        self._save()
        self.current_snapshot.font_size = font_size

    def get_font_size(self):
        return self.current_snapshot.font_size

    def undo(self):
        self._restore(self.history.pop())

    def _save(self):
        self.history.push(copy(self.current_snapshot))

    def _restore(self, state):
        self.current_snapshot = state if state else copy(
            self.default_state)

    class History:
        def __init__(self) -> None:
            self.states = []

        def push(self, state):
            self.states.append(state)

        def pop(self):
            return self.states.pop() if len(self.states) > 0 else None

    class Snapshot:
        def __init__(self, content, font_name, font_size) -> None:
            self.content = content
            self.font_name = font_name
            self.font_size = font_size


def test_editor_method(editor, editor_method, *args):
    print(f"Testing editor.{editor_method.__name__}.")
    print(f"Initial editor state -> {editor}.")
    for arg in args:
        editor_method(arg)
        print(f"* editor.{editor_method.__name__}({arg}) -> {editor}")
    print("------------")
    print("")


def test_undos(editor):
    print("A bit of undos...")
    editor.undo()
    print(editor)
    editor.undo()
    print(editor)
    print("------------")
    print("")


if __name__ == '__main__':
    editor = Editor()
    print(f"Initial editor -> {editor}")
    editor.undo()
    print(f"Initial undo -> {editor}")
    print("------------")
    print("")

    test_editor_method(editor, editor.set_content, "a", "b")
    test_undos(editor)
    test_editor_method(editor, editor.set_font_name,
                       "Victor Mono", "Fira Code")
    test_undos(editor)
    test_editor_method(editor, editor.set_font_size, 14, 24)
    test_undos(editor)
