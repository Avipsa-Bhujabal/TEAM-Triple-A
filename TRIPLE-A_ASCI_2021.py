#TEAM TRIPLE-A
import pyttsx3
import speech_recognition as s 
import datetime
import pywhatkit
import webbrowser
import wikipedia 
import wolframalpha
import pyjokes
from selenium import webdriver
from tkinter import *
from PIL import Image,ImageTk



app_id = ('AUXY7Y-8PWEUGTRL6')
user = wolframalpha.Client(app_id)


what = pyttsx3.init()
r = s.Recognizer()

# Speak function says the command to the user
def speak(text):
    what.say(text)
    what.runAndWait()
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

# Wishing me 
def greet():
    hr = datetime.datetime.now().hour
    if hr>=6 and  hr<12 :
        speak("GOOD MORNING " + Name)
    elif hr >=12 and hr<18 :
        speak("GOOD AFTERNOON " + Name)
    else :
        speak("GOOD EVENING " + Name)   

#take command from microphone
def order():
    speak("How may I help you"+ Name)
    try :
        with s.Microphone() as sr :
            print("Listening .... ")
            voice = r.listen(sr)
            speech = r.recognize_google(voice,language='en-in')
            print(speech)
    except Exception as e:
        speak("Sorry! Say that again")
        speech = None
    return speech

class gui() : #class for creating a GUI application
    def __init__(s):
        r = Tk()
        r.title('Jerry , The Virtual Assistant')
        r.geometry('1366x840')

        img = ImageTk.PhotoImage(Image.open("F:/23de5967e32e56bb06115e30ac5ef4a1.jpg")) #Adding image in the application
        panel = Label(r,image = img)
        panel.pack(side='left',fill='y',expand='no')

        s.ct = StringVar()
        s.ut = StringVar()

        s.ut.set("Click Run Jerry to Give Command")

        uf = LabelFrame(r,text='User', font=('Black Chancery',20,'bold','italic'),fg='black',height=300,width=200)
        uf.pack(fill='both',expand='yes')

        user=Message(uf,textvariable=s.ut,bg='#001f03',fg='#e0d100')
        user.config(font=('TIMES NEW ROMAN',30))
        user.pack(fill='both',expand='yes')



        cf = LabelFrame(r,text='Jerry', font=('Black Chancery',20,'bold','italic'),fg='black',height=300,width=200)
        cf.pack(fill='both',expand='yes')

        jerry=Message(cf,textvariable=s.ct,bg='#e0d100',fg='#001f03')
        jerry.config(font=('TIMES NEW ROMAN',30,'bold'))
        jerry.pack(fill='both',expand='yes')


        b1 = Button(r,text='RUN JERRY',font=('ATHLETIC',15,'bold'),bg='#959499',fg='black',command=s.clicked)
        b1.pack(fill='x',expand='yes')
        b2 = Button(r,text='STOP ME',font=('ATHLETIC',15,'bold'),bg='#959499',fg='black',command=r.destroy)
        b2.pack(fill='x',expand='yes')
        s.ct.set("Hi, I am Jerry!!! How can I help you?")
        r.mainloop()
    
    def clicked(self): #clicking button to execute task
        print('Working')
        self.ut.set('Listening....')
        speech=order()
        self.ut.set(speech)
        #Execution of task 
        if 'play' in speech :  #playing song on youtube
            song = speech.replace('play',' ')
            self.ct.set('playing'+song)
            speak('playing'+song)
            pywhatkit.playonyt(song)
        elif 'open Google' in speech : #opening google tab
            google = speech.replace('open','')
            self.ct.set('Opening'+google)
            speak('Opening'+google)
            webbrowser.open('www.google.com')
        elif 'search for ' in speech : #searching from wikipedia
            wiki = speech.replace('search for','')
            know = wikipedia.summary(wiki,3)
            self.ct.set(know)
            speak(know)
        elif 'joke' in speech : #To listen to joke
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            speak(joke)
        elif 'news' in speech:#To read news headlines
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
        elif 'open silicon ERP' in speech:#Automating SILICON ERP
            cpath="C:\\Users\mypc\chromedriver_win32\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=cpath)
            silicon=speech.replace("open","")
            self.ct.set("Opening "+silicon)
            speak("Opening "+silicon)
            driver.get('http://erp.silicon.ac.in/estcampus/')
            username = driver.find_element_by_xpath('//*[@id="username"]')
            username.send_keys('20bcsd08')
            password = driver.find_element_by_xpath('//*[@id="password"]')
            password.send_keys('2507July.')
            button = driver.find_element_by_css_selector('button[type=submit]')
            button.click()
        elif 'solve'or'weather'or'date'or'time' or 'who is' or 'what is' in speech: #to solve questions , get weather of a place , get date time and other gk
            res = user.query(speech)
            answer = next(res.results).text 
            self.ct.set(answer)
            speak(answer)
print("STARTING, JERRY YOUR PERSONAL VIRTUAL ASSISTANT ")
speak("STARTING, JERRY YOUR PERSONAL VIRTUAL ASSISTANT")
Name = take_name()
greet()
widget=gui()
  
        






