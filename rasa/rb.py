import pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Speak : ")
    audio = r.listen(source)
    print("Time Up.")
    print("Text: " + r.recognize_google(audio, language = 'Hi-IN'))
# try:
#     print("Text: " + r.recognize_google(audio, language = 'Hi-IN'))
    
# except:
#     pass



import pyaudio
import speech_recognition as sr
from translation import baidu, google, youdao, iciba
from googletrans import Translator
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Speak : ")
    audio = r.listen(source)
    print("Time Up.")
    #print("Text: " + r.recognize_google(audio, language = 'Hi-IN'))
# try:
#     text = print("Text: " + r.recognize_google(audio, language = 'Hi-IN'))
#     print("hindi",text)
#     translator = Translator()
#     print('hi')
#     english = print(translator.translate(r.recognize_google(audio, language = 'Hi-IN')))    
# except:
#     pass