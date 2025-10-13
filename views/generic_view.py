from datetime import datetime
from abc import ABC


class GenericView(ABC):
    def show_message(self, msg: str):
        print(f"\n{msg}")

    def propmt_user_yes_or_no(self, msg):
        print(f"\n{msg}")
        print("1 - Yes")
        print("2 - No")
        while True:
            value = self.input_int("Select: ")
            if value != 1 and value != 2:
                print("\nSelect a valid option")
            else:
                return True if value == 1 else False

    def input_int(self, msg):
        while True:
            try:
                value = input(msg)
                int_value = int(value)
                return int_value

            except ValueError:
                print("\n Please provide a valid int value")

    def input_specific_int(self, msg: str, valid_ints: list):
        while True:
            value = self.input_int(msg)
            if value not in valid_ints:
                print(f"\n Please provide a valid number, valid {valid_ints}")
            else:
                return value

    def input_string(self, msg):
        while True:
            value = input(msg)
            value = value.strip()
            if value:
                return value
            else:
                print("\n Provide a non empty text value")

    def input_date(self, msg):
        while True:
            input_date = input(msg)
            try:
                date = datetime.strptime(input_date, "%d/%m/%Y")
                return date
            except ValueError:
                print(f"\n Please provide a valid date on format DD/MM/YYYY\n")
