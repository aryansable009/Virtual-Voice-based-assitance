import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source)
            try:
                command = listener.recognize_google(voice)
                if 'cat' in command:
                    command = command.replace('cat', '')
                print(command)
            except:
                print("sorry, could not recognise")
    except:
        pass
    return command

isTrue = True
talk('sanket how may i help you')
def run_cat():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who  is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif ('joke' in command):
        talk(pyjokes.get_joke())

    elif 'quit' in command:
        isTrue = False
    else:
        talk('Please say the command again.')

while isTrue:
    run_cat()