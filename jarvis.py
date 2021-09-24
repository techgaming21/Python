import pyttsx3 # pip install pyttx3
import speech_recognition as sr # pip install SpeechRecognition
import datetime # inbuilt module of datetime
import os # inbuilt module of os(operating system)
import cv2 # pip install opencv-python

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text message
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    
    try:
        print("Recognizing sir...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Master said: {query}")

    except Exception as e:
        speak("Master please say again, I'm not unable to get it")
        return "none"
    return query

# To wish master
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning master")
    elif houe>12 and hour<17:
        speak("Good Afternoon master")
    else:
        speak("Good Evening master")
    speak("Hello master. PLease tell me how can i help you?")

if __name__ == "__main__":
    speak("This is advance E.D.I.T.H made by my master.")
    wish()
    #while True:
    if 1:
        query = takecommand()

        # Logic building for tasks
        if 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open code' in query:
            apath = "C:\\Users\\Microsoft\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(apath)
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open camera' in query:
            pass