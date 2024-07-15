from controllers.podcast_controller import PodcastController
from services.gpt_service import GPTService
from views.user_interface import UserInterface
from services.even_labs_service import ElevenLabsService
from dotenv import load_dotenv

import os


# Carregando as variáveis do arquivo .env
load_dotenv()

def carregar_servicos():
    api_key_openai = os.getenv('OPENAI_API_KEY')
    api_key_elevenlabs = os.getenv('ELEVENLABS_API_KEY')
    voice_id_elevenlabs = os.getenv('ELEVENLABS_VOICE_ID')
    
    gpt_service = GPTService(api_key_openai)
    elevenlabs_service = ElevenLabsService(api_key_elevenlabs, voice_id_elevenlabs)
    
    return gpt_service, elevenlabs_service

def criar_diretorio_podcast(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def obter_proximo_numero_arquivo(pasta, prefixo, extensao):
    arquivos = [nome for nome in os.listdir(pasta) if nome.startswith(prefixo) and nome.endswith(extensao)]
    arquivos.sort()
    if arquivos:
        ultimo_arquivo = arquivos[-1]
        ultimo_numero = int(ultimo_arquivo.split('-')[1].split('.')[0])
        return ultimo_numero + 1
    else:
        return 1

def salvar_roteiro(pasta, prefixo, numero, roteiro):
    caminho_arquivo_txt = os.path.join(pasta, f'{prefixo}-{numero:02d}.txt')
    with open(caminho_arquivo_txt, 'w') as file:
        file.write(roteiro)
    print(f'Roteiro salvo em: {caminho_arquivo_txt}')
    return caminho_arquivo_txt

def sintetizar_e_salvar_audio(elevenlabs_service, roteiro, pasta, prefixo, numero):
    caminho_arquivo_audio = os.path.join(pasta, f'{prefixo}-{numero:02d}.mp3')
    caminho_arquivo_audio = elevenlabs_service.sintetizar_voz(roteiro, caminho_arquivo_audio)
    if caminho_arquivo_audio:
        print(f'Áudio salvo em: {caminho_arquivo_audio}')
    else:
        print('Erro ao salvar o áudio.')
    return caminho_arquivo_audio

def main():
    gpt_service, elevenlabs_service = carregar_servicos()
    podcast_controller = PodcastController(gpt_service)
    user_interface = UserInterface()

    prompt = user_interface.get_user_prompt()
    podcast = podcast_controller.criar_podcast(prompt)
    user_interface.display_podcast(podcast)

    pasta = 'arquivos-podcast'
    criar_diretorio_podcast(pasta)

    proximo_numero = obter_proximo_numero_arquivo(pasta, 'podcast', '.txt')

    caminho_arquivo_txt = salvar_roteiro(pasta, 'podcast', proximo_numero, podcast.script)
    sintetizar_e_salvar_audio(elevenlabs_service, podcast.script, pasta, 'podcast', proximo_numero)

if __name__ == "__main__":
    main()