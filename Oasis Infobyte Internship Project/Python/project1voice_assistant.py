import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
#Imstall pip install SpeechRecognition pyttsx3 pywhatkit to run the code By Hitendra Yeole
# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice (optional: use female/male voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index if needed

def talk(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user voice input and return as text"""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Can you say it again?")
        return ""
    except sr.RequestError:
        talk("Oops, I can't connect to the service.")
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

def run_assistant():
    """Main function to run the assistant"""
    talk("Hello! How can I help you today?")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command:
            talk("Hey there!")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {current_time}")
        elif "date" in command:
            today = datetime.date.today()
            talk(f"Today's date is {today.strftime('%B %d, %Y')}")
        elif "search" in command:
            search_query = command.replace("search", "").strip()
            talk(f"Searching for {search_query}")
            pywhatkit.search(search_query)
        elif "stop processing" in command or "exit" in command or "quit" in command or "stop" in command:
            talk("Goodbye!")
            break
        else:
            talk("Sorry, I don't know that yet.")

if __name__ == "__main__":
    run_assistant()
