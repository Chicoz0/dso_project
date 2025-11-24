from views.generic_view import GenericView


class TagView(GenericView):
    def show_tag(self, tag_id: int, tag_name: str, tag_slug: str):
        msg = f"ID: {tag_id}\nName: {tag_name}\nShort: {tag_slug}"
        super().show_message(msg)

    def prompt_user_for_tag(self):
        tag_id = super().input_int("Select tag ID:")
        return tag_id if tag_id is not None else 0

    def show_tags_one_line(self, tags: list):
        msg = " - ".join(tags)
        self.popup_scrolled(f"Tags List:\n{msg}", title="Tags")

    def prompt_user_for_tag_info(self) -> str:
        return super().input_string("Enter Tag Name:")
