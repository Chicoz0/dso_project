from DAOs.dao import DAO
from models.event.tag import Tag


class TagDAO(DAO):
    def __init__(self):
        super().__init__("data/tags.pkl")

    def add(self, tag: Tag):
        if (tag is not None) and isinstance(tag, Tag):
            super().add(tag.id, tag)

    def update(self, tag: Tag):
        if (tag is not None) and isinstance(tag, Tag):
            super().update(tag.id, tag)

    def get(self, id: int):
        if isinstance(id, int):
            return super().get(id)

    def remove(self, id: int):
        if isinstance(id, int):
            return super().remove(id)
