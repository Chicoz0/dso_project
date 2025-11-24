from DAOs.dao import DAO


class UniversalID(DAO):
    def __init__(self):
        super().__init__("data/universal_id.pkl")

    def get_id(self):
        keys = list(self.get_keys())
        if keys:
            id = keys[0]
            self.remove(id)
            new_id = id + 1
            self.add(new_id, new_id)
        else:
            new_id = 1
            self.add(new_id, new_id)
        return new_id
