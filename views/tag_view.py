from views.generic_view import GenericView


class TagView(GenericView):
    def show_tag(self, tag_id: int, tag_name: str, tag_slug: str):
        print(f"\nID: {tag_id} - Name {tag_name}, Short: {tag_slug}")

    def prompt_user_for_tag(self):
        return super().input_int("\nSelect tag id: ")

    def show_tags_one_line(self, tags: list):
        msg = " - ".join(tags)
        print(f"Tags: {msg}")

    def prompt_user_for_tag_info(self) -> str:
        print("\n----- Tag Creation -----")
        tag_name = super().input_string("Enter Tag Name: ")
        return tag_name
