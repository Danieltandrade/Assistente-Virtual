"""
Arquivo principal do programa

Descrição:
    Este arquivo contém o código principal do programa, onde o usuário pode escolher entre escrever ou falar.

Bibliotecas:
    datetime: Biblioteca para trabalhar com datas e horários.
    playsound3: Biblioteca para reproduzir arquivos de audio.
    src.get_audio: Função que recebe o audio e retorna a frase.
    src.text_to_speech: Função que recebe o texto e retorna o audio.
    webbrowser: Biblioteca para abrir sites na web.

Functions:
    main(): Função principal do programa.

Exemplo de uso:
    python main.py
"""
from datetime import datetime
from playsound3 import playsound
from src import get_audio
from src import text_to_speech

import webbrowser

def main():
    """
    Função principal do programa.

    Exemplo de uso:
        python main.py
    """

    print("Bem-vindo ao assistente de voz!\n")
    while True:

        user_input = input("Digite uma das opções abaixo:\n1 - Escrever\n2 - Falar\n0 - Sair\n-> ")
        # Configurando idioma.
        language = "pt"
        tld = "com.br"

        match user_input: # Escolhendo opção

            case "1": # Convertendo texto em voz

                text = input("Digite o texto a ser convertido em voz: ")
                file = "audio1.mp3"
                tts = text_to_speech(text, language, tld, file)

                if tts:
                    print("Texto convertido em voz com sucesso!")
                else:
                    print("Erro ao converter o texto em voz.")
                    print(tts)

            case "2": # Convertendo audio em texto

                language = "pt-BR"
                frase = get_audio(language)
                # Reconhecendo audio
                if frase == "Abrir YouTube":
                    url = "https://www.youtube.com/"
                    webbrowser.open(url, new=1, autoraise=True)

                elif frase == "Abrir Google":
                    url = "https://www.google.com/"
                    webbrowser.open(url, new=1, autoraise=True)

                elif frase == "data e hora atual":
                    text = f"""
                        Hoje é dia {datetime.now().strftime('%d/%m/%Y')} e agora são 
                        {datetime.now().strftime('%H:%M:%S')}.
                    """
                    file = "audio2.mp3"

                    tts = text_to_speech(text, language, tld, file)

                    if tts:
                        playsound(f"audios/{file}")
                    else:
                        print("Erro ao converter o texto em voz.")
                        print(tts)

                elif frase == "sair":
                    print("Saindo...")
                    break

            case "0": # Sair
                print("Saindo...")
                break

if __name__ == "__main__":
    main()
