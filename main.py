import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # [0] is male voice and [1] is female voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning my dear friend")
    elif 12 <= hour < 18:
        speak("Good Afternoon my dear friend")
    else:
        speak("Good Evening my dear friend")
    speak("I am your personal assistant, How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you chandan...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice....")
        query = r.recognize_google(audio, language='en-in')
        print(f"My dear friend you said : {query}\n")

    except Exception as e:
        print("chandan say that again please......")
        return "None"

    return query


def open_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(result)
    speak(result)


def open_application(application_path):
    os.startfile(application_path)


def open_website(url):
    webbrowser.open(url)


def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"My dear friend, the time is {strTime}")


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<EMAIL>', '<PASSWORD>')
    server.sendmail('<FROM_EMAIL>', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            open_wikipedia(query)

        elif 'open notepad' in query:
            notepad_path = "paste path location"  # Replace with actual path
            open_application(notepad_path)

        elif 'open paint' in query:
            paint_path = "paint path location"  # Replace with actual path
            open_application(paint_path)

        elif 'open youtube' in query:
            open_website("https://www.youtube.com")

        elif 'open facebook' in query:
            open_website("https://www.facebook.com")

        elif 'open google' in query:
            open_website("https://www.google.com")

        elif 'tell me the time' in query:
            tell_time()

        elif 'open linkedin' in query:
            open_website("https://www.linkedin.com")
