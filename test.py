import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import ctypes
import pyjokes





engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

print(voice[1].id)
engine.setProperty('voice', voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 






def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Sir I am Jarvis, How may I Help You")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)ex
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        # elif 'Hello Jarvis' or 'Jarvis' in query:
        #     speak("Yes Sir")
                

        # elif 'Jarvis tell me a joke' or 'tell me a joke'in query:
        #     while True:
        #         speak(pyjokes.get_joke())
        #         time.sleep(10)
        #         break
                
                
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        # elif 'tell me a riddle' in query:
        #     open('C:\voice\ridd')
        #     speak('ridd.txt')

        elif 'open google' in query:
            speak('yes sir')
            webbrowser.open("google.com")
        
        elif 'open My mail' in query:
            speak('yes sir')
            webbrowser.open("gmail.com")

        elif 'open spotify' in query:
            speak('yes sir')
            webbrowser.open('spotify.com')

        elif 'lock window' in query:
            speak('locking the device')
            ctypes.windll.user32.LockWorkStation()
        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif 'play music' in query:
            music_dir = 'C:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))
         
        
        elif 'play video' in query:
            video_dir = 'C:\Videos'
            video = os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir, video[0]))
          

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

       
        elif "shut up" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
       
            
        

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to aruna' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gopalaruna2001@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Bharath. I am not able to send this email")    

       