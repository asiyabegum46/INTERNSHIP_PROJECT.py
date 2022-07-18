import pyttsx3 as p
import pywhatkit
import datetime
import wikipedia
import pyjokes

import speech_recognition as sr
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
print(voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()
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
        text = r.recognize_google(audio)
    if "information" in text:
        speak("you need information related to which topic")


with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        speak("searching {} in wikipedia".format(infor))

        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get(url="https://www.wikipedia.org/")

        if"play"in text:
          speak("playing in youtube")
driver.maximize_window()
driver.get(url = 'https://www.youtube.com/')





#driver.find_element_by_xpath('//*[@id="dismissable"]')
#driver.find_element_by_name()



#def play(self, query):
    #self.query = query
    #self.driver.get(url="https://www.youtube.com//results?search_query="+ query)
    #video= self.driver.find_element_by_xpath('//*[@id="dismissable"]')
    #video.click()


#assist.play('dynamite by bts')
