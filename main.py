"""

"""

from src import get_audio
from src import text_to_speech

def main():

    print("Bem-vindo ao assistente de voz!\n")
    while True:
        user_input = input("Digite uma das opções abaixo:\n1 - Escrever\n2 - Falar\n0 - Sair\n -> ")
        match user_input:

            case "1": # Convertendo texto em voz
                # Exemplo de entrada de texto.
                input_user={
                    "text": "Olá, meu nome é Mary. Tudo bem com você?",
                    "language": "pt",
                    "tld": "com.br",
                    "file": "audio1.mp3"
                }

                confirm = text_to_speech(
                    input_user["text"], 
                    input_user["language"], 
                    input_user["tld"], 
                    input_user["file"]
                )

                if confirm:
                    print("Texto convertido em voz com sucesso!")
                else:
                    print("Erro ao converter o texto em voz.")
                    print(confirm)

            case "2": # Convertendo audio em texto
                # Exemplo de entrada de audio.
                language = "pt-BR"
                frase = get_audio(language)
                print(frase)

            case "0": # Sair
                print("Saindo...")
                break

if __name__ == "__main__":
    main()
