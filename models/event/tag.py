from DAOs.ids_dao import UniversalID


class Tag:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name:
            raise Exception("Invalid name")

        self.__id = UniversalID().get_id()
        self.__name = name
        self.__slug = self.generate_slug(name)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name
        self.__name = self.generate_slug(new_name)

    @property
    def slug(self):
        return self.__slug

    def generate_slug(self, name: str):
        return name.strip().replace(" ", "_").lower()
