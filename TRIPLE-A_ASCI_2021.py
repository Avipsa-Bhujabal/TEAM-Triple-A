#TEAM TRIPLE-A
import pyttsx3
import speech_recognition as s 
import datetime
import pywhatkit
import webbrowser
import wikipedia 
import wolframalpha
import pyjokes

app_id = ('AUXY7Y-8PWEUGTRL6')
user = wolframalpha.Client(app_id)

print("STARTING, JERRY YOUR PERSONAL VIRTUAL ASSISTANT ")
what = pyttsx3.init()
r = s.Recognizer()

# Speak function says the command to the user
def speak(text):
    what.say(text)
    what.runAndWait()

speak("STARTING, JERRY YOUR PERSONAL VIRTUAL ASSISTANT")

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

while True :

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
    if 'play' in speech :  #playing song on youtube
        song = speech.replace('play',' ')
        print('playing'+song)
        speak('playing'+song)
        pywhatkit.playonyt(song)
    elif 'open Google' in speech : #opening google tab
        google = speech.replace('open','')
        print('Opening'+google)
        speak('Opening'+google)
        webbrowser.open('www.google.com')
    elif 'who is ' in speech : #searching for famous person in wikipedia
        wiki = speech.replace('who is ','')
        know = wikipedia.summary(wiki,3)
        print(know)
        speak(know)
    elif 'what is ' in speech : #searching any stuff in wikipedia
        wiki = speech.replace('what is ','')
        know = wikipedia.summary(wiki,3)
        print(know)
        speak(know)
    elif 'joke' in speech :
        joke = pyjokes.get_joke(language="en", category="all")
        print(joke)
        speak(joke)
    elif 'stop' in speech : #breaking the loop of taking command 
        speak('OK!BYE ')
        speak('Have a nice day')
        break
    elif 'solve'or'weather'or'date'or'time' in speech: #to solve questions , get weather of a place and get date time
        res = user.query(speech)
        answer = next(res.results).text 
        print(answer)
        speak(answer)
  
        






