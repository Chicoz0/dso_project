from utils.id import generate_id


class Attraction:
    def __init__(self, name: str, attraction_type: str):
        if not isinstance(name, str) or not name:
            raise Exception("Invalid name")

        if not isinstance(attraction_type, str) or not attraction_type:
            raise Exception("Invalid Attraction Type")

        self.__id = generate_id()
        self.__name = name
        self.__attraction_type = attraction_type

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str) or not new_name:
            raise Exception("Invalid name")

        self.__name = new_name

    @property
    def attraction_type(self):
        return self.__attraction_type

    @attraction_type.setter
    def attraction_type(self, new_attraction_type: str):
        if not isinstance(new_attraction_type, str) or not new_attraction_type:
            raise Exception("Invalid attraction_type")

        self.__attraction_type = new_attraction_type
