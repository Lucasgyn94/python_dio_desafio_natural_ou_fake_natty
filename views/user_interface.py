class UserInterface:
    def get_user_prompt(self):
        return input("Digite as informações para o roteiro do podcast: ")

    def display_podcast(self, podcast):
        print("\n--- Roteiro do Podcast ---")
        print(podcast.script)
