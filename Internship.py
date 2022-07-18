import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 130)
voices = speaker.getProperty('voices')
speaker.setProperty("voice", voices[1].id)


def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def take_command():
     command =''


listener = sr.Recognizer()
speak("hello madam,i'm your hey siri. how are you?")

with sr.Microphone() as source:
    listener.energy_threshold = 10000
    listener.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    print(command)
if "what" and "about" and "you" in command:
    speak("i am also having a good day madam")

    speak("what can i do for you??")
sr.Microphone(device_index=1)

listener = sr.Recognizer()

listener.energy_threshold =5000

with sr.Microphone() as source:
    print("speak!")
    voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        print("you said :{}".format(command))
        url = 'https://www.google.co.in/search?q='
        search_url = url + command
        webbrowser.open(search_url)

    except:

        print("can't recognize")