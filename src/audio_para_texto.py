"""
Arquivo para reconhecer o audio e retornar a frase

Bibliotecas:
    speech_recognition: Biblioteca do Google para reconhecer o audio

Functions:
    get_audio(lang): Reconhece o audio e retorna a frase

Exemplo de uso:
    language = "pt-BR"
    get_audio(language)
"""

import speech_recognition as sr

def get_audio(lang):
    """
    Função que recebe o audio e retorna a frase

    Args:
        lang (str): O idioma do audio.

    Returns:
        str: A frase reconhecida.

    Raises:
        Exception: Se ocorrer um erro ao reconhecer o audio.

    Example:
        language = "pt-BR"
        get_audio(language)
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
    try:
        frase = recognizer.recognize_google(audio, language=lang)
        print(f"Você disse: {frase}")
        return frase
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro ao se conectar com o serviço de reconhecimento.")
    return None
