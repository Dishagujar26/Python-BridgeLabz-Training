import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()

    if "open google" in command:
        wb.open("https://www.google.com")

    elif "open facebook" in command:
        wb.open("https://www.facebook.com")

    elif "open youtube" in command:
        wb.open("https://www.youtube.com")

    elif "open instagram" in command:
        wb.open("https://www.instagram.com")

    elif command.startswith("play"):
        song = command.replace("play", "").strip()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            wb.open(link)
        else:
            speak("Sorry, I could not find that song.")

if __name__ == "__main__":
    speak("Hello, I am your virtual assistant.")
    speak("Initializing Jarvis.")

    while True:
        print("Recognizing wake word...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active... Speak your command.")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                process_command(command)

        except Exception as e:
            print("Error:", e)