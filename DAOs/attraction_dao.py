from DAOs.dao import DAO
from models.event.attraction import Attraction


class AttractionDAO(DAO):
    def __init__(self):
        super().__init__("data/attractions.pkl")

    def add(self, attraction: Attraction):
        if (attraction is not None) and isinstance(attraction, Attraction):
            super().add(attraction.id, attraction)

    def update(self, attraction: Attraction):
        if (attraction is not None) and isinstance(attraction, Attraction):
            super().update(attraction.id, attraction)

    def get(self, id: int):
        if isinstance(id, int):
            return super().get(id)

    def remove(self, id: int):
        if isinstance(id, int):
            return super().remove(id)
