#speach to text
import speech_recognition as sr
import pyaudio
def stt():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Speak : ")
        audio = r.listen(source)
        print("Time Up.")
        #print("Text: " + r.recognize_google(audio, language = 'Hi-IN'))
    try:
        text = r.recognize_google(audio, language = 'En-IN')
        print("Your text is :",text)
        return text    
    except:
        return print("sorry can't hear")
        # pass;
        
# stt()