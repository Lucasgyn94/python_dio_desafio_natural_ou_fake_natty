import requests

class ElevenLabsService:
    def __init__(self, api_key, voice_id):
        self.api_key = api_key
        self.voice_id = voice_id

    def sintetizar_voz(self, texto, caminho_arquivo):
        CHUNK_SIZE = 1024
        tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}/stream"

        headers = {
            "Accept": "application/json",
            "xi-api-key": self.api_key
        }

        data = {
            "text": texto,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True
            }
        }

        response = requests.post(tts_url, headers=headers, json=data, stream=True)

        if response.ok:
            with open(caminho_arquivo, "wb") as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)
            print("Audio stream saved successfully.")
            return caminho_arquivo
        else:
            print(response.text)
            return None
