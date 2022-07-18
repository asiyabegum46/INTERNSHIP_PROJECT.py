import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import pyaudio
import pywhatkit
import pyjokes



listener = sr.Recognizer()
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 130)
voices = speaker.getProperty('voices')
speaker.setProperty("voice", voices[1].id)



def speak(text):
    speaker.say(text)
    speaker.runAndWait()


va_namme = 'alexa'


def take_command():
    command = ''

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

    listener.energy_threshold = 5000

    with sr.Microphone() as source:
        print("speak!")
        voice = listener.listen(source)


    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command .replace(va_name + '', '')
                print(command)
                speak(command)
    except:
        print('check your microphone ')
    return command
while True:
    user_command = take_command()
    if 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M:%P")
        print(cur_time)
        speak(cur_time)
        break
    elif 'play' in user_command:
        user_command = user_command . replace('play','')
        print('playing '+ user_command)
        speak('playing '+ user_command + ', enjoy.')
        pywhatkit.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for', '')
        user_command = user_command.replace('google','')
        speak ('searching for'+user_command)
        pywhatkit.search(user_command)
        break
    elif 'who is ' in user_command:
        user_command = user_command.replace('who is', '')
        info = wikipedia.summary(user_command ,2)
        print(info)
        speak(info)
        break
