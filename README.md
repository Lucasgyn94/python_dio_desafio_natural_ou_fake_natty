# Podcast Generator 🎙️
Bem-vindo ao Podcast Generator, um projeto inovador que mistura a capacidades avançada de duas grandes IA's generativas para gerar roteiros de podcasts, sintetizar voz e produzir conteúdos de áudio de alta qualidade. Utilizando o poder do ChatGPT para criar roteiros e ElevenLabs para a síntese de voz, este projeto automatiza a criação de podcasts, tornando o processo eficiente e acessível.

### 🧐 Processo de Criação
Entrada do Usuário: O usuário fornece um prompt descrevendo o tema do podcast.
Geração do Roteiro: Utilizando a OpenAI API, um roteiro detalhado é criado com base no prompt.
Salvamento do Roteiro: O roteiro é salvo em um arquivo de texto com um nome sequencial.
Síntese de Voz: O texto do roteiro é convertido em um arquivo de áudio MP3 usando a ElevenLabs API.
Armazenamento: Os arquivos de texto e áudio são armazenados em uma estrutura organizada para fácil acesso e edição.

## Funcionalidades
Geração de Roteiros: Utiliza o ChatGPT para criar roteiros de podcast baseados em prompts fornecidos pelo usuário.
Síntese de Voz: Converte roteiros de texto em arquivos de áudio usando a IA de ElevenLabs.
Armazenamento Organizado: Salva os roteiros e arquivos de áudio em uma estrutura de diretórios organizada.

## 🚀 Resultados
O Podcast Generator facilita a produção de podcasts, permitindo a criação rápida e eficiente de conteúdos de áudio de alta qualidade. Os resultados incluem roteiros bem elaborados e arquivos de áudio prontos para edição e publicação. Cada episódio é armazenado de forma organizada, pronto para ser utilizado ou editado conforme necessário.

## 🤖 Tecnologias Utilizadas
Python<br>
OpenAI API (ChatGPT)<br>
ElevenLabs API (sintetização de voz)<br>

## Estrutura do Projeto
podcast_generator/<br>
├── arquivos-podcast/<br>
├── controllers/<br>
│   ├── __init__.py<br>
│   └── podcast_controller.py<br>
├── main.py<br>
├── models/<br>
│   ├── __init__.py<br>
│   └── podcast.py<br>
├── poetry.lock<br>
├── pyproject.toml<br>
├── services/<br>
│   ├── gpt_service.py<br>
│   ├── elevenlabs_service.py<br>
│   └── __init__.py<br>
└── views/<br>
    ├── __init__.py<br>
    └── user_interface.py<br>

## Como Executar
### Pré-requisitos
Python 3.11+<br>
Poetry (para gerenciar dependências)<br>

### Passos para Execução
Clone este repositório:<br>
sh<br>
git clone https://github.com/seu-usuario/podcast-generator.git<br>
cd podcast-generator<br>

### Instale as dependências:
sh<br>
poetry install<br>

### Configure suas chaves de API no arquivo .env:
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:<br>

OPENAI_API_KEY=your_openai_api_key_here<br>
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here<br>
ELEVENLABS_VOICE_ID=your_elevenlabs_voice_id_here<br>

### Execute o projeto:
sh<br>
poetry run python podcast_generator/main.py<br>

### Exemplo de Uso
Após iniciar o script, você será solicitado a fornecer um prompt para o roteiro do podcast. O roteiro será gerado e salvo como um arquivo de texto, e a voz será sintetizada e salva como um arquivo MP3 na pasta arquivos-podcast.<br>
EX: <br>Crie um roteiro para um podcast de 5 minutos que explique o que são IAs Generativas, suas aplicações e impactos na tecnologia moderna.


### Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para adicionar novas funcionalidades, corrigir bugs ou melhorar a documentação.

### Licença
Este projeto está licenciado sob a MIT License.

### Contato
Para mais informações, entre em contato com needslucas944@gmail.com
