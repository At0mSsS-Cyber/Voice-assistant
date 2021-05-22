import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
active = 0


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'alexa' in command:
                talk('Yes sir')
                print('Listening....')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                return command
    except:
        pass
    


def run_alexa():
    command = take_command()
    print(command)
    if(command == None):
        pass
    else:
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'shutdown' in command:
            talk('Roger that')
            exit()
        elif 'what is your name' in command:
            talk('By calling my name you are asking my name. That does not make sense')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'what' in command:
            person = command.replace('what is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'how old are you' in command:
            talk('I just born now. Only few hours old')
        else:
            talk('Please say the command again.')
        
        
while True:
    run_alexa()