import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning ")

    elif hour>=12 and hour<17 :
        speak("Good Afternoon")

    else :
        speak("Good Night") 

    speak("I am Zen . Please say how can I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening... ")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query) 
    
    except Exception as e:

        print("say again please")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    f = open('myfile.txt','r')
    while True:
         query = takeCommand().lower()

         # logic for tasks 

         if 'wikipedia' in query:
            speak("searching wikipedia... ")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

         elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

         elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

         elif 'open gfg' in query:
            webbrowser.open("https://www.geeksforgeeks.org/ ")

         elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

         elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak("the time is {}".format(strTime)) 
        
         elif 'open code' in query:
            codePath = "C:\\Users\\Sanskar Gupta\\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

         elif 'yourself' in query:
            speak("my name is Zen. i am a desktop assistant, i am able to open any application or any websites for you ")
         
         elif 'github' in query:
            webbrowser.open("https://github.com/")

         elif 'reminder' in query:

            for rm in f:
                print(rm)
                speak(rm)

         elif 'stop execution ' in query:
            exit()
  
