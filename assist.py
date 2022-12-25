from bs4 import BeautifulSoup
from flask import request_started
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import pywhatkit as kit
import wikipedia
import webbrowser
import requests
import sys
import pyjokes 
import pyautogui
import time
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
       self.JARVIS()
    

#to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
    try:
        print("Recog......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
        speak(f"user said: {query}")
    except Exception as e:
        speak("Say that again please.....")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
      speak("Good Morning")
    elif hour>=12 and hour<18:
      speak("Good Afternoon")
    else:
      speak("Good evening")
    
    speak("I am Quest made by MindBenders please tell me  how can I help you?")





if __name__ =="__main__":
    wish()
    while True:
    #if 1:
        query = takecommand().lower()

        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open  VS code' in query:
            codePath = "C:\\Users\\shivani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open  Microsoft Team' in query:
            mPath = "C:\\Users\\shivani\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart\\Teams.exe"
            
            os.startfile(mPath)  
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")
        elif 'open google' in query:
                webbrowser.open('www.google.co.in')
        elif " open flipkart" in query:
            webbrowser.open("www.flipkart.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open wikipedia" in query:
            webbrowser.open("www.wikipedia.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open whatsapp" in query:
            webbrowser.open("www.whatsapp.com")
        elif "open amazon" in query:
            webbrowser.open("www.amazon.com")
        elif " open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "github" in query:
            webbrowser.open("www.github.com")
        elif "open mail" in query:
            webbrowser.open("www.gmail.com")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(58)
               if k == 27:
                  break
            cap.release()
            cv2.destroyAllWindows()
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address id {ip}") 
        
        elif "temperature" in query:
           search = "temperature in sagar"
           url = f"https://www.google.com/search?q={search}"
           r = requests.get(url)
           data = BeautifulSoup(r.text, "html.parser")
           temp = data.find("div",class_="BNeawe").text
           speak(f"current {search} is {temp}")
        elif "search" in query and "google" in query:
            query = query.replace("search","")
            query = query.replace("on google","")
            query = query.replace("google","")
            string = query.split()
            search = ""
            for i in string:
             search += i
    
             search += "+"

            webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")
        elif "wikipedia" in query:
            query = query.replace("on wikipedia","")
            query = query.replace("wikipedia","")
            query = query.replace("search","")
            speak(f"searching {query} on wikipedia")
            results = wikipedia.summary(query,sentences = 2)
            speak("here are the results")
            print(results)
            speak(results)
        elif "search" in query and "youtube" in query :
            query = query.replace("search","")
            query = query.replace("on youtube","")
            query = query.replace("youtube","")
            string = query.split()
            search = ""
            for i in string:
                search += i
    
                search += "+"
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
        elif 'open my current location' in query:
            def My_Location():
                op = "https://www.google.com/maps/place/Indira+Gandhi+Engineering+College/@23.8696711,78.8151579,17z/data=!3m1!4b1!4m5!3m4!1s0x3978d1c981eeed05:0x9dcd43dc9133a52a!8m2!3d23.8696662!4d78.8173466"

                webbrowser.open(op)
                ip_add = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
                geo_q = requests.get(url)
                     
            My_Location()    

        ## r = sr.Recognizer()
           # with sr.Microphone() as source:
               ## speak("Say what you want to calculate, example: 3 plus 3")
               # print("listening..........")
               # r.adjust_for_ambient_noise(source)
               # audio = r.listen(source)
            #my_string.recognize_google(audio)
           # print(my_string)
            #def get_operator_fn(op):
              # return{
                  ## '+' : operator.add,
                  # '-' : operator.sub,
                  # '*' : operator.mul,
                   #'divided' : operator._

              #  }
        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("mam, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for second, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done mam, the screenshot is saved inour main folder. now i am ready for next command")
        
        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
             import psutil
             battery = psutil.sensors_battery()
             percentage = battery.percent
             speak(f"mam our system have {percentage} percent battery")
             if percentage>=75:
                 speak("we have enough power to continue our work")
             elif percentage>=40 and percentage<=75:
                 speak("we should connect our system to charging point to charge our battery")
             elif percentage<=15 and percentage<=30:
                 speak("we don't have enough power to work, please connect to charging")
             elif percentage<=15:
                 speak("we have very low power, please connect to charging the system will shutdown very soon")
        
        elif 'internet speed' in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"mam we have {dl} bit per second downloading speed and {up} bit per second uploading speed ")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'tell me a news' in query:
            speak("please wait sir, fetching the largest news")
           # news()
        
        elif 'switch  the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'shut down the system' in query:
            os.system("shutdown /s /t S")
    

        elif 'restart the system' in query:
            os.system("shutdown /r /t S")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

        
        
        elif 'close notepad' in query:
            speak("Okay mam, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close youtube' in query:
            speak("Okay mam, closing youtube")
            webbrowser.close("taskkill /f /im www.youtube.com")
        elif 'no thanks' in query:
            speak('thanks for using me mam, have a good day')
            sys.exit()
        speak('mam, do you have any other work')  
        

       # elif 'send message' in query:
           # kit.sendwhatmsg("+919876543210", "This is testing protocol", 2,24)
        #elif 'play songs on youtube' in query:
         #   kit.playanysong("wake up")
    #takecommand()
    #speak("hello mam")
    #speak("hello mam")
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())