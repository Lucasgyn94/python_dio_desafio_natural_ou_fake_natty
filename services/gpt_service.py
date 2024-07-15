from openai import OpenAI

class GPTService:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def gerar_script(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800
        )
        script = response.choices[0].message.content.strip()
        return script
