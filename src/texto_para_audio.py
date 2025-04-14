"""
Arquivo para converter o texto em voz

Bibliotecas:
    gtts: Biblioteca do Google para converter o texto em voz

Functions:
    text_to_speech(text, language, tld, file): Converte o texto em voz e salva o arquivo de audio

Exemplo de uso:
    text = "Olá, meu nome é Mary. Tudo bem com você?"
    language = "pt"
    tld = "com.br"
    file = "audio1.mp3"
"""

from gtts import gTTS

def text_to_speech(text, language, tld, file) -> bool:
    """
    Converte o texto em voz e salva o arquivo de audio.

    Args:
        text (str): O texto a ser convertido em voz.
        language (str): O idioma do texto.
        tld (str): O domínio do idioma.
        file (str): O nome do arquivo de audio.

    Returns:
        bool: True se o arquivo de audio foi salvo com sucesso, False caso contrário.

    Raises:
        Exception: Se ocorrer um erro ao converter o texto em voz.
    """
    try:
        tts = gTTS(text, lang=language, tld=tld)
        tts.save(f"audios/{file}")
        return True
    except Exception as e:
        return e
