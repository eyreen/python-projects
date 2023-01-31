import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print('Hi I am Jonas')
engine.say('Hi I am Jonas')
print('What can I do for you')
engine.say('What can I do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jonas' in command:
                print(command)
    except:
        pass
    return command

def run_jonas():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'Who are you' or 'Can you tell me about yourself' in command:
        print('I am Jonas, a virtual assistant created on 24th June 2022 by Arinn Danish')
        talk('I am Jonas, a virtual assistant created on 24th June 2022 by Arinn Danish')
    else:
        print('Please say the command again')


while True:
    run_jonas()