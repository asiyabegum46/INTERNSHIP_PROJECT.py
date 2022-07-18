
import pyttsx3 as p
import pywhatkit
import datetime
import wikipedia
import pyjokes

import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
print(voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_siri():
    command = r.listen()
    print(command)


r = sr.Recognizer()
speak("hello Madam i'm your voice assistant. how are you??")

with sr.Microphone() as source:
    r.energy_threshold =10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio =r.listen(source)
    text = r.recognize_google(audio)
    print(text)

  if "what" and "about" and "you" in text:
        speak("i am also having a good day madam")
        speak("what can i do for you??")

with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)



    if "information" in text2:
        speak("you need information related to which topic")


    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        speak("searching {} in wikipedia".format(infor))
    if 'play' in text:
        song = text.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)


















