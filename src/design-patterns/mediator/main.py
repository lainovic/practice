from abc import ABC, abstractmethod
from re import S, T
from tkinter import E


class UIControl:
    def __init__(self, owner: 'DialogBox') -> None:
        self.owner = owner


class ListBox(UIControl):
    def __init__(self, owner: 'DialogBox') -> None:
        super().__init__(owner)
        self.selection = ""

    def set_selection(self, selection: str) -> None:
        self.selection = selection
        self.owner.changed(self)


class TextBox(UIControl):
    def __init__(self, owner: 'DialogBox') -> None:
        super().__init__(owner)
        self.content = ""

    def set_content(self, content: str) -> None:
        self.content = content
        self.owner.changed(self)


class Button(UIControl):
    def __init__(self, owner: 'DialogBox') -> None:
        super().__init__(owner)
        self.enabled = True

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled
        self.owner.changed(self)


class DialogBox(ABC):
    @abstractmethod
    def changed(self, control: UIControl):
        pass


class ArticlesBox(DialogBox):
    def __init__(self) -> None:
        self.articles_list_box = ListBox(self)
        self.title_text_box = TextBox(self)
        self.save_button = Button(self)

    def simulate_demo(self):
        print(f"* Select Lorem Ipsum in the article...")
        self.articles_list_box.set_selection("Lorem Ipsum")
        print(f"Title: {self.title_text_box.content}")
        print(f"Save button status: {self.save_button.enabled}")
        print(f"* Remove the title...")
        self.title_text_box.set_content("")
        print(f"Save Button status: {self.save_button.enabled}")
        print(f"* Set new title...")
        self.title_text_box.set_content("FooBar")
        print(f"Save Button status: {self.save_button.enabled}")

    def changed(self, control: UIControl) -> None:
        if control is self.articles_list_box:
            self._on_article_selected()
        elif control is self.title_text_box:
            self._on_title_changed()

    def _on_article_selected(self) -> None:
        self.title_text_box.set_content(self.articles_list_box.selection)
        self.save_button.set_enabled(True)

    def _on_title_changed(self) -> None:
        is_empty = self.title_text_box is None or len(
            self.title_text_box.content) == 0
        self.save_button.set_enabled(not is_empty)


class EventHandler(ABC):
    @abstractmethod
    def handle(self):
        pass


class UIControlV2:
    def __init__(self) -> None:
        self.event_handlers = []

    def add_event_hander(self, event_handler: EventHandler) -> None:
        self.event_handlers.append(event_handler)

    def _notify(self):
        for handler in self.event_handlers:
            handler.handle()


class ListBoxV2(UIControlV2):
    def __init__(self) -> None:
        super().__init__()
        self.selection = ""

    def set_selection(self, selection: str) -> None:
        self.selection = selection
        self._notify()


class TextBoxV2(UIControlV2):
    def __init__(self) -> None:
        super().__init__()
        self.content = ""

    def set_content(self, content: str) -> None:
        self.content = content
        self._notify()


class ButtonV2(UIControlV2):
    def __init__(self) -> None:
        super().__init__()
        self.enabled = False

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled
        self._notify()


class CheckBoxV2(UIControlV2):
    def __init__(self) -> None:
        super().__init__()
        self.checked = False

    def set_checked(self, checked) -> None:
        self.checked = checked
        self._notify()


class SignUpDialogBox():
    def __init__(self) -> None:
        def create_event_handler(action):
            def create_type(**kwargs):
                return type("", (object,), kwargs)
            return create_type(handle=action)

        self.username_box = TextBoxV2()
        self.password_box = TextBoxV2()
        self.checkbox = CheckBoxV2()
        self.signup_button = ButtonV2()

        enable_button_action = create_event_handler(
            action=self.on_control_changed)
        self.username_box.add_event_hander(enable_button_action)
        self.password_box.add_event_hander(enable_button_action)
        self.checkbox.add_event_hander(enable_button_action)

    def simulate_demo(self):
        print(f"Button status: {self.signup_button.enabled}")
        print("* Fill out the username: lajkabaus")
        self.username_box.set_content("lajkabaus")
        print(f"Button status: {self.signup_button.enabled}")
        print("* Fill out the password: ********")
        self.password_box.set_content("********")
        print(f"Button status: {self.signup_button.enabled}")
        print("* Check that you agree with terms and conditions")
        self.checkbox.set_checked(True)
        print(f"Button status: {self.signup_button.enabled}")
        print("* Remove the password.")
        self.password_box.set_content("")
        print(f"Button status: {self.signup_button.enabled}")
        print("* Re-set the password: ********")
        self.password_box.set_content("********")
        print(f"Button status: {self.signup_button.enabled}")

    def on_control_changed(self) -> None:
        self.signup_button.set_enabled(len(self.username_box.content) > 0 and
                                       len(self.password_box.content) > 0 and
                                       self.checkbox.checked)


if __name__ == "__main__":
    dialog = ArticlesBox()
    dialog.simulate_demo()

    print('------------------------------------------------------------------------')

    dialog = SignUpDialogBox()
    dialog.simulate_demo()
