# Assistente-Virtual

[![Python Version](https://img.shields.io/badge/Python-3.10|3.11|3.12|3.13-blue.svg)](https://www.python.org/downloads/)
[![Last Update](https://img.shields.io/github/last-commit/Danieltandrade/Assistente-Virtual.svg)](https://github.com/Danieltandrade/Assistente-Virtual)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/Danieltandrade/Assistente-Virtual/actions)

Este é um projeto de assistente virtual que permite ao usuário escolher entre escrever ou falar. O assistente pode converter texto em voz e voz em texto, além de realizar ações específicas com base nas frases reconhecidas.

## Funcionalidades

- Conversão de texto em voz
- Conversão de voz em texto
- Reconhecimento de frases específicas para realizar ações
- Abertura de sites na web

## Tecnologias Utilizadas

- Linguagem Python
- Bibliotecas:
    - gTTS
    - playsound3
    - PyAudio
    - SpeechRecognition
    - Webbrowser

## Instalação

1. Certifique-se de ter o Python 3.10 ou superior instalado em seu computador.
2. Clone o repositório do projeto utilizando o comando `git clone https://github.com/Danieltandrade/Assistente-Virtual.git`.
3. Navegue para a pasta do projeto utilizando o comando `cd Assistente-Virtual`.
4. Instale as bibliotecas necessárias utilizando o comando `pip install -r requirements.txt`.
5. Execute o programa utilizando o comando `python main.py`
6. Siga as instruções do assistente virtual para interagir com ele.

> [!WARNING]
> Para que o programa funcione, é necessário um microfone conectado ao computador.

## Exemplo de uso

Abaixo temos um exemplo de uso do programa, onde ele irá converter o texto em voz e reconhecer o audio, realizando ações com base na frase.

```bash
Bem-vindo ao assistente de voz!

Digite uma das opções abaixo:
1 - Escrever
2 - Falar
0 - Sair
-> 1
Digite o texto a ser convertido em voz: Boa noite.
Texto convertido em voz com sucesso!
# "audio1.mp3" criado com a fala "Boa noite."
Fale algo...
Você disse: contrato e hora atual
Digite uma das opções abaixo:
1 - Escrever
2 - Falar
0 - Sair
-> 2
# O programa fala a data e hora atual, que foi salva em "audio2.mp3"
Fale algo...
Você disse: data e hora atual
Digite uma das opções abaixo:
1 - Escrever
2 - Falar
0 - Sair
-> 0
Saindo...
# Programa finalizado com sucesso!
```

## Estrutura do projeto

Abaixo é apresentado a estrutura do projeto, contendo os arquivos e pastas principais:

```bash
Assistente-Virtual/
├── audios/
│   ├── audio1.mp3
│   └── audio2.mp3
├── src/
│   ├── __init__.py
│   ├── audio_para_texto.py
│   └── texto_para_audio.py
├── __version__.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── main.py
```

## Licenca

Este projeto é licenciado sob a licenca [MIT](https://github.com/Danieltandrade/Assistente-Virtual/blob/main/LICENSE).

## Contribuições

Se vocé deseja contribuir para o projeto, sinta-se livre para abrir uma issue ou enviar um pull request.

## Contato

Para entrar em contato com o desenvolvedor, visite o perfil do GitHub [Danieltandrade](https://github.com/Danieltandrade), ou envie um e-mail para [danieltorresandrade@gmailcom](mailto:danieltorresandrade@gmail.com).

## Conclusão

O projeto apresentou o comportamento esperado, sendo capaz de converter o texto em voz e reconhecer o audio, realizando ações com base nas frases. Claro que, comparado as LLMs que temos hoje, ele será muito mais simples e limitado. Espero que sirva de ajuda e inspiração para quem busca desenvolver um assistente virtual.

__Grande abraços a todos!__