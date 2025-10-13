class TagView:
    def show_tag(self, tag_id: int, tag_name: str, tag_slug: str):
        print(f"\n ID: {tag_id} - Name {tag_name}, Short: {tag_slug}\n")

    def prompt_user_for_tag_info(self) -> str:
        print("\n----- Tag Creation -----")
        tag_name = input("Enter Tag Name: ")
        return tag_name

    def show_message(self, msg: str):
        print(f"\n{msg}\n")
