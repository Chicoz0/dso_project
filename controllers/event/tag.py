from models.event.tag import Tag


class TagController:
    def __init__(self):
        self.__tags = []

    @property
    def tags(self):
        return self.__tags

    def create_tag(self, name: str):
        tag = Tag(name)

        for t in self.tags:
            if tag.slug == t.slug:
                return

        self.tags.append(tag)
