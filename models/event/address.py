from utils.id import generate_id


class Address:
    def __init__(
        self, street: str, suite: str, neighborhood: str, city: str, zip_code: str
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

        self.__id = generate_id()
        self.__street = street
        self.__suite = suite
        self.__neighborhood = neighborhood
        self.__city = city
        self.__zip_code = zip_code

    @property
    def id(self):
        return self.__id

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, new_street: str):
        self.__street = new_street

    @property
    def suite(self):
        return self.__suite

    @suite.setter
    def suite(self, new_suite: str):
        self.__suite = new_suite

    @property
    def neighborhood(self):
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, new_neighborhood: str):
        self.__neighborhood = new_neighborhood

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city: str):
        self.__city = new_city

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code: str):
        self.__zip_code = new_zip_code
