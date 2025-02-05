import speech_recognition as sr
import pyttsx3
import os
import urllib.parse
import datetime
import webbrowser
import pyautogui
import time

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Converts text to speech and speaks it out loud."""
    print(f"Jarvis: {text}")
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
    """Opens a website."""
    speak(f"Opening {site_name}...")
    webbrowser.open(url)

def open_youtube():
    """Opens YouTube."""
    speak("Opening YouTube...")
    webbrowser.open("https://www.youtube.com")

def open_google():
    """Opens Google."""
    speak("Opening Google...")
    webbrowser.open("https://www.google.com")

def search_youtube(query):
    """Searches YouTube for the given query."""
    query_encoded = urllib.parse.quote_plus(query)
    speak(f"Searching YouTube for {query}...")
    url = f"https://www.youtube.com/results?search_query={query_encoded}"
    webbrowser.open(url)

def play_youtube_video(video_name):
    """Plays a YouTube video."""
    video_encoded = urllib.parse.quote_plus(video_name)
    speak(f"Playing {video_name} on YouTube...")
    url = f"https://www.youtube.com/results?search_query={video_encoded}&sp=EgIQAw%253D%253D"
    webbrowser.open(url)

def search_google(query):
    """Searches Google for the given query."""
    query_encoded = urllib.parse.quote_plus(query)
    speak(f"Searching Google for {query}...")
    webbrowser.open(f"https://www.google.com/search?q={query_encoded}")

def check_time():
    """Tells the current time."""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def open_system_application(command):
    """Opens various system applications based on command."""
    apps = {
        "notepad": "notepad.exe",
        "chrome": "chrome",
        "calculator": "calc",
        "file explorer": "explorer",
        "task manager": "taskmgr",
        "control panel": "control"
    }
    
    for app in apps:
        if app in command:
            speak(f"Opening {app}...")
            os.system(apps[app])
            return True
    return False

def system_control(command):
    """Handles system commands like shutdown, restart, log off."""
    if "shutdown" in command:
        speak("Shutting down the system...")
        os.system("shutdown /s /t 5")
    elif "restart" in command:
        speak("Restarting the system...")
        os.system("shutdown /r /t 5")
    elif "log off" in command:
        speak("Logging off...")
        os.system("shutdown /l")

def open_any_application(command):
    """Opens any application by name."""
    app_name = command.replace("open", "").strip()
    speak(f"Opening {app_name}...")
    os.system(f"start {app_name}")

def show_desktop():
    """Shows the desktop by minimizing all windows."""
    speak("Showing the desktop...")
    pyautogui.hotkey('win', 'd')

def switch_to_vs_code():
    """Brings Visual Studio Code to the foreground."""
    speak("Switching to Visual Studio Code...")
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')  # Repeat the Alt+Tab to land on VS Code

# Main loop
while True:
    command = listen()
    
    if command is None:
        continue
    
    if "jarvis" in command:
        speak("Yes sir?")
    elif "how are you" in command:
        speak("I am fine.")
    elif "salam walekum" in command:
        speak("Walkum Assalam")
    elif "allah hafiz" in command:
        speak("Allah Hafiz")
        break
    elif "open youtube" in command:
        open_youtube()
    elif "open google" in command:
        open_google()
    elif "open" in command:
        open_any_application(command)
    elif "search youtube for" in command:
        video_name = command.replace("search youtube for", "").strip()
        search_youtube(video_name)
    elif "play" in command and "youtube" in command:
        video_name = command.replace("play", "").replace("on youtube", "").strip()
        play_youtube_video(video_name)
    elif "search google for" in command:
        search_query = command.replace("search google for", "").strip()
        search_google(search_query)
    elif "what time is it" in command or "current time" in command:
        check_time()
    elif "shutdown" in command or "restart" in command or "log off" in command:
        system_control(command)
    elif "open the desktop" in command:
        show_desktop()
    elif "back to vs code" in command:
        switch_to_vs_code()
    elif "bye" in command or "goodbye" in command:
        speak("Goodbye, sir!")
        break
    else:
        speak("I don't understand that command.")
