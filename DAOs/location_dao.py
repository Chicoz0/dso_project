from DAOs.dao import DAO
from models.location.location import Location


class LocationDAO(DAO):
    def __init__(self):
        super().__init__("data/locations.pkl")

    def add(self, location: Location):
        if (location is not None) and isinstance(location, Location):
            super().add(location.id, location)

    def update(self, location: Location):
        if (location is not None) and isinstance(location, Location):
            super().update(location.id, location)

    def get(self, id: int):
        if isinstance(id, int):
            return super().get(id)

    def remove(self, id: int):
        if isinstance(id, int):
            return super().remove(id)
