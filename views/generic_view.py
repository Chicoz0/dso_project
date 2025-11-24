import FreeSimpleGUI as sg

from datetime import datetime
from abc import ABC


class GenericView(ABC):
    def __init__(self):
        self.__window = None
        self.__header_size = 60
        self.__title_size = 40
        self.__normal_size = 20
        self.__font = "Helvica"

    @property
    def window(self):
        return self.__window

    def popup_scrolled(self, msg, title):
        font = (self.__font, self.__normal_size)
        return sg.popup_scrolled(msg, title=title, font=font)

    def header(self, msg):
        font = (self.__font, self.__header_size)
        return sg.Text(msg, font=font)

    def title(self, msg):
        font = (self.__font, self.__title_size)
        return sg.Text(msg, font=font)

    def input_title(self, msg):
        font = (self.__font, self.__normal_size)
        return sg.Text(msg, font=font)

    def button(self, msg):
        font = (self.__font, self.__normal_size)
        return sg.Button(msg, font=font)

    def button_key(self, msg, key):
        font = (self.__font, self.__normal_size)
        return sg.Button(msg, font=font, key=key)

    def cancel(self):
        font = (self.__font, self.__normal_size)
        return sg.Cancel("Cancel", font=font)

    def confirm(self):
        font = (self.__font, self.__normal_size)
        return sg.Button("Confirm", font=font)

    def input_text(self, key):
        font = (self.__font, self.__normal_size)
        return sg.InputText("", key=key, font=font)

    def radio(self, text, group, key):
        font = (self.__font, self.__normal_size)
        return sg.Radio(text, group, key=key, font=font)

    @window.setter
    def window(self, w):
        self.__window = w

    def popup(self, msg):
        font = (self.__font, self.__normal_size)
        sg.popup("", msg, font=font)

    def close(self):
        if self.window:
            self.window.Close()

    def read_window(self):
        button = 0
        values = {}
        if self.window:
            button, values = self.window.Read()
        return button, values

    def show_message(self, msg: str):
        font = (self.__font, self.__normal_size)
        sg.popup(msg, title="Info", font=font)

    def propmt_user_yes_or_no(self, msg):
        font = (self.__font, self.__normal_size)
        answer = sg.popup_yes_no(msg, title="Question", font=font)
        return True if answer == "Yes" else False

    def input_int(self, msg):
        font = (self.__font, self.__normal_size)
        while True:
            value = sg.popup_get_text(msg, title="Input Required", font=font)

            if value is None:
                return None

            try:
                return int(value)
            except ValueError:
                sg.popup("Please provide a valid integer value", font=font)

    def input_specific_int(self, msg: str, valid_ints: list):
        font = (self.__font, self.__normal_size)
        while True:
            value = self.input_int(f"{msg}\nValid options: {valid_ints}")
            if value is None:
                return None

            if value not in valid_ints:
                sg.popup(f"Please provide a valid number from: {valid_ints}", font=font)
            else:
                return value

    def input_string(self, msg):
        font = (self.__font, self.__normal_size)
        while True:
            value = sg.popup_get_text(msg, title="Input Required", font=font)

            if value is None:
                return ""

            value = value.strip()
            if value:
                return value
            else:
                sg.popup("Provide a non-empty text value", font=font)

    def input_date(self, msg):
        font = (self.__font, self.__normal_size)
        while True:
            input_date = sg.popup_get_text(
                f"{msg} (Format: DD/MM/YYYY)", title="Date Input", font=font
            )

            if input_date is None:
                return None

            try:
                date = datetime.strptime(input_date, "%d/%m/%Y")
                return date
            except ValueError:
                sg.popup("Please provide a valid date in format DD/MM/YYYY", font)
