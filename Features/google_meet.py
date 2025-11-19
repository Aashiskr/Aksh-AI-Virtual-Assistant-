import os
import webbrowser
import time
import pyautogui
import pyperclip
import speech_recognition as sr
from TextToSpeech import Fast_DF_TTS

def get_active_url():
    try:
        pyautogui.hotkey('alt', 'd')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)
        return pyperclip.paste()
    except Exception as e:
        return None

def create_meet_link(meeting_time):
    # 1. Open Google Meet
    webbrowser.open("https://meet.google.com/new")
    time.sleep(6)

    # 2. Copy Link
    link = get_active_url()

    if link:
        # 3. Save to the NEW file
        # UPDATED FILE NAME BELOW:
        file_path = "meeting_schedule_data.txt"

        with open(file_path, "a") as f:
            f.write(f"Time: {meeting_time} | Link: {link}\n")
        return link
    else:
        return None


import speech_recognition as sr

def take_command():
    # 1. Initialize the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # 2. Adjust for background noise
        r.pause_threshold = 1
        r.energy_threshold = 300

        # START LOOP: Keep listening until we get a valid result
        while True:
            try:
                Fast_DF_TTS.speak("Tell me the Time Sir...")
                # 3. Capture the audio
                # (Added phrase_time_limit to stop it from listening forever if background is noisy)
                audio = r.listen(source, timeout=5, phrase_time_limit=10)

                print("Recognizing...")
                # 4. Convert Audio to Text
                query = r.recognize_google(audio, language='en-in') # type: ignore
                print(f"User said: {query}\n")

                # IF WE REACH HERE, IT WORKED -> Return the text
                return query.lower()

            except Exception as e:
                # If an error occurs (silence or noise), just print this and LOOP AGAIN
                print("Say that again please...")
                continue
