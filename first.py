import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import urllib.parse

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Faster response speed
engine.setProperty('volume', 1.0)  # Max volume

# Set the voice (this may vary depending on your system, Windows/Mac/Linux)
voices = engine.getProperty('voices')

# Set a nice voice (you can try different indexes for different voices)
engine.setProperty('voice', voices[1].id)  # For a female voice, try voices[1]
# For a male voice, try voices[0]

def speak(text):
    """Converts text to speech and speaks it out loud."""
    print(f"Jarvis: {text}")  # Debugging print
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to user input via microphone and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("I didn't understand.")
            return None
        except sr.RequestError:
            print("Speech recognition API error.")
            return None

def open_website(url, site_name):
    """Opens a website using OS system command."""
    speak(f"Opening {site_name}...")
    os.system(f"start {url}")  # Works faster than webbrowser.open()

def search_youtube(query):
    """Searches YouTube for the given query (video or channel)."""
    query_encoded = urllib.parse.quote_plus(query)  # Encode query for URL
    speak(f"Searching YouTube for {query}...")
    search_url = f"https://www.youtube.com/results?search_query={query_encoded}"
    os.system(f"start {search_url}")

def open_youtube_channel(channel_name):
    """Opens a YouTube channel."""
    channel_encoded = urllib.parse.quote_plus(channel_name)  # Encode channel name
    speak(f"Opening YouTube channel {channel_name}...")
    channel_url = f"https://www.youtube.com/c/{channel_encoded}"
    os.system(f"start {channel_url}")

def open_youtube_live(channel_name):
    """Opens live stream of a YouTube channel."""
    if "madni channel" in channel_name.lower():
        live_url = "https://www.youtube.com/c/MadniChannel/live"  # Madni Channel live stream URL
        speak("Opening live stream of Madni Channel...")
        os.system(f"start {live_url}")
    else:
        channel_encoded = urllib.parse.quote_plus(channel_name)  # Encode channel name
        live_url = f"https://www.youtube.com/c/{channel_encoded}/live"
        speak(f"Opening live stream of {channel_name}...")
        os.system(f"start {live_url}")

def search_google(query):
    """Searches Google for the given query."""
    query_encoded = urllib.parse.quote_plus(query)  # Encode query for URL
    speak(f"Searching Google for {query}...")
    search_url = f"https://www.google.com/search?q={query_encoded}"
    os.system(f"start {search_url}")

# Main loop
while True:
    command = listen()
    
    if command is None:
        continue  # Skip if no command was heard

    if "jarvis" in command:
        speak("Yes sir?")

    elif "open notepad" in command:
        speak("Opening Notepad...")
        os.system("notepad.exe")

    elif "open chrome" in command:
        speak("Opening Chrome...")
        os.system("start chrome")

    elif "open youtube" in command:
        speak("Opening YouTube...")
        os.system("start https://www.youtube.com")

    elif "search youtube for" in command:
        video_name = command.replace("search youtube for", "").strip()
        search_youtube(video_name)

    elif "open youtube channel" in command:
        channel_name = command.replace("open youtube channel", "").strip()
        open_youtube_channel(channel_name)

    elif "open live stream of" in command:
        channel_name = command.replace("open live stream of", "").strip()
        open_youtube_live(channel_name)

    elif "open google" in command:
        speak("Opening Google...")
        os.system("start https://www.google.com")

    elif "search google for" in command:
        search_query = command.replace("search google for", "").strip()
        search_google(search_query)

    elif "open calculator" in command:
        speak("Opening Calculator...")
        os.system("calc")

    elif "exit" in command or "goodbye" in command:
        speak("Goodbye, sir!")
        break

    else:
        speak("I don't understand that command.")

