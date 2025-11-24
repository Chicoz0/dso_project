import FreeSimpleGUI as sg

from datetime import datetime
from abc import ABC


class GenericView(ABC):
    def __init__(self):
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, w):
        self.__window = w

    def popup(self, msg):
        sg.popup("", msg)

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
        sg.popup(msg, title="Info")

    def propmt_user_yes_or_no(self, msg):
        answer = sg.popup_yes_no(msg, title="Question")
        return True if answer == "Yes" else False

    def input_int(self, msg):
        while True:
            value = sg.popup_get_text(msg, title="Input Required")
 
            if value is None:
                return None

            try:
                return int(value)
            except ValueError:
                sg.popup("Please provide a valid integer value")

    def input_specific_int(self, msg: str, valid_ints: list):
        while True:
            value = self.input_int(f"{msg}\nValid options: {valid_ints}")
            if value is None:
                return None

            if value not in valid_ints:
                sg.popup(f"Please provide a valid number from: {valid_ints}")
            else:
                return value

    def input_string(self, msg):
        while True:
            value = sg.popup_get_text(msg, title="Input Required")

            if value is None: # Cancel
                return ""

            value = value.strip()
            if value:
                return value
            else:
                sg.popup("Provide a non-empty text value")

    def input_date(self, msg):
        while True:
            input_date = sg.popup_get_text(f"{msg} (Format: DD/MM/YYYY)", title="Date Input")
 
            if input_date is None:
                return None

            try:
                date = datetime.strptime(input_date, "%d/%m/%Y")
                return date
            except ValueError:
                sg.popup("Please provide a valid date in format DD/MM/YYYY")
