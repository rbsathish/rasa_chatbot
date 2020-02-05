#text to speach
from gtts import gTTS 
import os 
def tts(text):
    # Language in which you want to convert 
    language = 'en'
    sentence = text.replace('\'', '')
    print("sentence",sentence)
    texttospeech = gTTS(text=sentence, lang=language, slow=False)
    texttospeech.save("reply.wav")
    os.system("reply.wav")
    return texttospeech