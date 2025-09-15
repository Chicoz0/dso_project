from models.location.address import Address


class Location:
    def __init__(
        self,
        name: str,
        street: str,
        suite: str,
        neighborhood: str,
        city: str,
        zip_code: str,
    ):
        if not isinstance(name, str) or not name:
            raise Exception("Invalid name")

        if not isinstance(street, str) or not street:
            raise Exception("Invalid street")

        if not isinstance(suite, str) or not suite:
            raise Exception("Invalid suite")

        if not isinstance(neighborhood, str) or not neighborhood:
            raise Exception("Invalid neighborhood")

        if not isinstance(city, str) or not city:
            raise Exception("Invalid city")

        if not isinstance(zip_code, str) or not zip_code:
            raise Exception("Invalid zip_code")

        self.__name = name
        self.__address = Address(street, suite, neighborhood, city, zip_code)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str) or not new_name:
            raise Exception("Invalid name")
        self.__name = new_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(
        self,
        street: str,
        suite: str,
        neighborhood: str,
        city: str,
        zip_code: str,
    ):
        if not isinstance(street, str) or not street:
            raise Exception("Invalid street")

        if not isinstance(suite, str) or not suite:
            raise Exception("Invalid suite")

        if not isinstance(neighborhood, str) or not neighborhood:
            raise Exception("Invalid neighborhood")

        if not isinstance(city, str) or not city:
            raise Exception("Invalid city")

        if not isinstance(zip_code, str) or not zip_code:
            raise Exception("Invalid zip_code")

        self.__address = Address(street, suite, neighborhood, city, zip_code)
