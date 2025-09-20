from controllers.event.tag import TagController


class TagView:
    def __init__(self):
        self.__controller = TagController()

    @property
    def controller(self):
        return self.__controller

    def list_tags(self):
        print("Here are all the tags")
        for tag in self.controller.tags:
            print(f"ID: {tag.id} Tag: {tag.name} Slug: {tag.slug}")

    def create_tag(self):
        print("To create a tag, insert a name")
        name = input("name: ")

        try:
            self.controller.create_tag(name)
            print("Tag created!")
        except:
            print("Error while creating tag")
