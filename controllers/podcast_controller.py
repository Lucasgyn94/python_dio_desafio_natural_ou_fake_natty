from models.podcast import Podcast
from services.gpt_service import GPTService

class PodcastController:
    def __init__(self, gpt_service):
        self.gpt_service = gpt_service

    def criar_podcast(self, prompt):
        script = self.gpt_service.gerar_script(prompt)
        return Podcast(script)