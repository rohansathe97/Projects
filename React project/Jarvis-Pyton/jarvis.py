import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    
    speak("Hi I am Edith.")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" Good Moring! How may i help you?")
    elif hour>=12 and hour<16:
        speak("Good Afternoon! How may i help you?")
    else:
        speak("Good Night! How may i help you?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)

        print("Sorry Sir, I didn't quite get your command.")
        return "None"
    return query
    
if __name__ == "__main__":
    wish()
    command()
