#TEAM TRIPLE-A
import pyttsx3
import speech_recognition as s 
import datetime
import pywhatkit

print("STARTING, JERRY THE JARVIS ")
what = pyttsx3.init()
r = s.Recognizer()

# Speak function says the command to the user
def speak(text):
    what.say(text)
    what.runAndWait()

speak("STARTING, JERRY THE JARVIS")

#Taking name of user
def take_name():
    speak("Who are you?")
    try :
         with s.Microphone() as sr :
             print("Listening .... ")
             voice = r.listen(sr)
             name = r.recognize_google(voice)
             print(name)
    except : 
        pass
    return name

Name = take_name()
# Wishing me 
def greet():
    hr = datetime.datetime.now().hour
    if hr>=6 and  hr<12 :
        speak("GOOD MORNING " + Name)
    elif hr >=12 and hr<18 :
        speak("GOOD AFTERNOON " + Name)
    else :
        speak("GOOD EVENING " + Name)
greet()

#take command from microphone
def order():
    speak("How may I help you"+ Name)
    try :
         with s.Microphone() as sr :
             print("Listening .... ")
             voice = r.listen(sr)
             speech = r.recognize_google(voice)
             print(speech)
    except :
        pass
    return speech
speech = order()

#Execution of task 
if 'play' in speech :
        song = speech.replace('play',' ')
        print('playing'+song)
        speak('playing'+song)
        pywhatkit.playonyt(song)


        






