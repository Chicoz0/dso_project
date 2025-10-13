from typing import Optional
from models.event.tag import Tag

from views.tag_view import TagView


class TagController:
    def __init__(self):
        self.__tags = []
        self.__tag_view = TagView()

    @property
    def tags(self):
        return self.__tags

    def get_tag_by_id(self, id: int):
        for tag in self.tags:
            if tag.id == id:
                return tag
        return None

    def get_tag_by_name(self, name: str):
        for tag in self.tags:
            if tag.name == name:
                return tag
        return None

    def select_tag_by_id(self):
        tag_id = self.__tag_view.prompt_user_for_tag()
        tag = self.get_tag_by_id(tag_id)

        if tag:
            return tag
        self.__tag_view.show_message(f"Tag with ID {tag_id} not found")
        return None

    def show_tags(self, tags: list):
        slugs = [tag.slug for tag in tags]
        self.__tag_view.show_tags_one_line(slugs)

    def list_tags(self, tags: Optional[list] = None):
        tags = tags if tags else self.tags
        for tag in self.tags:
            self.__tag_view.show_tag(tag.id, tag.name, tag.slug)

    def delete_tag(self, id: int):
        tag = self.get_tag_by_id(id)
        if tag:
            self.tags.remove(tag)
            self.__tag_view.show_message(f"Tag with ID {tag.id} deleted!")
        else:
            self.__tag_view.show_message(f"Tag with ID {id} not found!")
        return

    def create_tag(self):
        tag_name = self.__tag_view.prompt_user_for_tag_info()
        tag_name = tag_name.lower()

        if not self.get_tag_by_name(tag_name):
            tag = Tag(tag_name)
            self.tags.append(tag)
            self.__tag_view.show_message(
                f"Tag ID {tag.id} and slug {tag.slug} created!"
            )
            return

        self.__tag_view.show_message("Tag already existed!")
