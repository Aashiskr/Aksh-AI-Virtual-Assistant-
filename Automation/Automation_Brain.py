from Automation.open_App import open_App
from Automation.Web_open import openweb
import pyautogui as gui
from Automation.Play_Music_YT import play_music_on_youtube
from TextToSpeech import Fast_DF_TTS
from  Automation.playmusic_Sfy import play_music_on_spotify
from Automation.call import call_the_person
from Automation.message import message_the_person
from Data.DLG_Data import jokes
from Automation.poem import play_poem
import random
import time
from Automation.Battery import check_percentage
from os import getcwd
from Automation.tab_automation import perform_browser_action
from Automation.Youtube_play_back import perform_youtube_action
import pywhatkit
from Features.check_internet_speed import get_internet_speed
from Automation.talking_games import talking_games
from TextToSpeech import hindispeak
import speech_recognition as sr

# Make sure you have this function defined clearly
def take_command():
    # 1. Initialize the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # 2. Adjust for background noise
        r.pause_threshold = 1
        r.energy_threshold = 300

        # 3. Listen (with a timeout so it doesn't hang forever)
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=5)
        except Exception as e:
            print("Listening timed out. No audio detected.")
            return "None"

    try:
        print("Recognizing...")
        # 4. Convert Audio to Text
        query = r.recognize_google(audio, language='en-in') # type: ignore
        print(f"User said: {query}")

    except Exception as e:
        # If it couldn't understand the audio
        print("Say that again please...")
        return "None"

    return query.lower()

def close():
    gui.hotkey('alt', 'f4')

def search_google(text):
    pywhatkit.search(text) # type: ignore

def kill_program():
    gui.hotkey('ctrl', 'C')

def tab_close():
    gui.hotkey('ctrl','w')

def minimize_window():
    # Pressing twice ensures it minimizes even if the window is fully maximized
    gui.hotkey('win', 'down')
    gui.hotkey('win', 'down')

def maximize_window():
    gui.hotkey('win', 'up')


def minimize_all():
    # This minimizes EVERYTHING and shows the desktop
    gui.hotkey('win', 'd')

def search(text):
    gui.press("/")
    time.sleep(2)
    gui.write(text)
    gui.press("enter")

def clear_file():
    with open(f"{getcwd()}\\input.txt","w")as file:
            file.truncate(0)



def Open_Brain(text):
    if "open" in text and "website" in text:
        text = text.replace("open", "").strip()
        text = text.replace("website", "").strip()
        text = text.replace("open website", "").strip()
        text = text.replace(" ", "").strip()
        openweb(text)

    else:
        text = text.replace("open app", "").strip()
        text = text.replace("open", "").strip()
        open_App(text)

def Auto_main_brain(text):
        if text.startswith("open"):
            Open_Brain(text)
        if "close this" in text:
            close()
        if "kill" in text:
            kill_program()
        if "tab close" in text:
            tab_close()
        if "minimize window" in text or "minimize this window" in text or "minimize current window" in text or "minimize" in text or "minimise" in text:
            minimize_window()
        if "minimize all" in text or "show desktop" in text:
            minimize_all()
        if "maximize window" in text or "maximize this window" in text or "maximize current window" in text or "maximize" in text:
            maximize_window()

        if "play video" in text or "play video on youtube" in text:
            Fast_DF_TTS.speak("Which video do you want to play sir")
            clear_file()
            output_text = ""
            while True:
                with open("input.txt","r")as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if output_text:
                        play_music_on_youtube(output_text)
                        break
                else:
                    pass
        if "play music" in text or "play music on spotify" in text:
            Fast_DF_TTS.speak("Which song do you want to play sir")
            time.sleep(1)
            clear_file()
            output_text = ""
            while True:
                with open("input.txt","r")as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if output_text:
                        play_music_on_spotify(output_text)
                        break
                else:
                    pass
        if "play games" in text or "switch game" in text:
            Fast_DF_TTS.speak("OK boss, let's play a game.")
            time.sleep(0.5)
            Fast_DF_TTS.speak("Which type of game do you want to play — virtual games or talking games?")
            clear_file()

            output_text = ""
            while True:
                with open("input.txt", "r") as file:
                    input_text = file.read().lower()
                if input_text != output_text:
                    output_text = input_text
                    if "virtual games" in output_text:
                        Fast_DF_TTS.speak("OK boss, let's play a virtual game.")
                        openweb("game")
                        break
                    elif "talking games" in output_text:
                        Fast_DF_TTS.speak("OK boss, let's play a talking game.")
                        clear_file()
                        talking_games()
                        break
                    elif "close" in output_text or "quit" in output_text:
                        Fast_DF_TTS.speak("Exiting the game. Goodbye!")
                        break
                    else:
                        Fast_DF_TTS.speak("Please say 'virtual games' or 'talking games'.")



        if "any joke" in text or "tell me a joke" in text or "tell me joke" in text or "joke sunao" in text:

            selected_joke = random.choice(jokes)
            hindispeak.speak2("here is joke for you")
            time.sleep(2)
            hindispeak.speak2(selected_joke)
            clear_file()

        if "any poem" in text:
            Fast_DF_TTS.speak("Here is you poem sir")
            time.sleep(1)
            play_poem()
            clear_file()
        if "take screenshot" in text:
            Fast_DF_TTS.speak("Taking screenshot")
            time.sleep(1)
            gui.hotkey('win', 'shift', 's')
            Fast_DF_TTS.speak("Select the area and save where you want save it")
            time.sleep(1)

        if "battery" in text or "batery" in text or "charge" in text:
            if "check percentage" in text or "percentage" in text or "charge kitna hai" in text or "check" in text or "kitna hai" in text:
                check_percentage()

        if "call" in text or "phone" in text:
            if "call someone" in text or "i want to call" in text or "make a call" in text or "call the person" in text or "call the contact" in text or "call kro" in text or "call karna hai" in text:
                Fast_DF_TTS.speak("Please tell me the name of the person you want to call")
                time.sleep(2)
                clear_file()
                output_text = ""
                while True:
                    with open("input.txt","r")as file:
                        input_text = file.read().lower()
                    if input_text != output_text:
                        output_text = input_text
                        if output_text:
                            call_the_person(output_text)
                            break
        if "message" in text or "sandesh" in text or "send message" in text:
            if "message someone" in text or "i want to message" in text or "send a message" in text or "message the person" in text or "message the contact" in text or "message kro" in text or "message karna hai" in text:
                Fast_DF_TTS.speak("Please tell me the name of the person you want to message")
                time.sleep(2)
                clear_file()
                output_text = ""
                while True:
                    with open("input.txt","r")as file:
                        input_text = file.read().lower()
                    if input_text != output_text:
                        output_text = input_text
                        if output_text:
                            message_the_person(output_text)
                            break
        if "search in google" in text or " google search" in text:
            text = text.replace("search in google", "").strip()
            text = text.replace("google search", "").strip()
            text = text.replace("search", "").strip()
            search_google(text)

        if text.startswith("search"):
            text = text.replace("search", "").strip()
            search(text)

        if "internet" in text and "speed" in text:
            if "check" in text or "test" in text or "measure" in text or "checking" in text or "testing" in text or "measuring" in text or "kya hai" in text:
                Fast_DF_TTS.speak("Checking internet speed")
                time.sleep(2)
                speed = get_internet_speed()
                Fast_DF_TTS.speak(f"Your internet speed is {speed} Mbps")

        if "hello aksh" in text or "hi aksh" in text or "hey aksh" in text:
            Fast_DF_TTS.speak("Hello sir, how can I help you?")
            time.sleep(1)
            clear_file()

        if "shutdown" in text or "shut down" in text or "band karo" in text:
            if "shut down computer" in text or "shut down the computer" in text or "computer shutdown" in text or "computer band karo" in text or "computer" in text or "the computer" in text:
                Fast_DF_TTS.speak("Shutting down the computer")
                time.sleep(2)
                gui.hotkey('win', 'x')
                time.sleep(1)
                gui.press('u')
                time.sleep(1)
                Fast_DF_TTS.speak("Goodbye sir, see you next time")
                time.sleep(1)
                gui.press('u')
                time.sleep(1)

        if "meeting" in text or "meeting link" in text:
            if "schedule" in text or "create" in text or "set up" in text or "set" in text or "new meeting" in text:
                from Features.google_meet import create_meet_link, take_command

                Fast_DF_TTS.speak("Ok sir i am scheduling a meeting for you.")

                # Listen for the time (e.g., "10 AM" or "5 PM")
                meeting_time = take_command()

                if meeting_time:
                    Fast_DF_TTS.speak("Okay, creating a new Google Meet link now...")

                    # This opens the browser and creates the link
                    new_link = create_meet_link(meeting_time)

                    if new_link:
                        Fast_DF_TTS.speak(f"Meeting scheduled for {meeting_time}. I have saved the link in your schedule file.")
                    else:
                        Fast_DF_TTS.speak("I opened the meeting, but I couldn't copy the link automatically.")

        if "send" in text and "meeting link" in text:
            # Example: "Send 9pm meeting link to Aditya"
            from Features.whatsapp_meeting_sender import send_specific_meeting

            # Pass the full query so the function can extract time and name
            send_specific_meeting(text)
        if "switch to" in text or "switch" in text or "change window to" in text:
            from Automation.window_switcher import switch_to_app

            # Remove the "switch to" part to get the app name
            # Example: "Switch to Brave" -> "brave"
            app_name = text.replace("switch to", "").strip()or text.replace("change window to", "").strip()or text.replace("switch", "").strip()

            if app_name:
                Fast_DF_TTS.speak(f"Switching to {app_name}...")
                found = switch_to_app(app_name)

                if not found:
                    Fast_DF_TTS.speak(f"I couldn't find a window named {app_name} open.")
            else:
                Fast_DF_TTS.speak("Which app should I switch to?")
        # if "check what is in my hand" in text or "read this" in text or "read prescription" in text:
        #     from Features.vision import check_what_is_in_hand

        #     Fast_DF_TTS.speak("Okay, hold it steady in front of the camera. Capturing in 3 seconds.")

        #     # Call the function
        #     result = check_what_is_in_hand()

        #     # Speak the result
        #     print(f"AI Saw: {result}")
        #     Fast_DF_TTS.speak(result)
        # elif "save email" in text or "save mail" in text or "add email" in text:
        #     from Features.email_sender import save_new_email, parse_email_from_voice

        #     # 1. Ask for the Name
        #     speak("Whose email do you want to save?")
        #     name = take_command()

        #     if name == "none":
        #         speak("I didn't hear a name. Cancelling.")
        #         continue # Skip to next loop iteration

        #     # 2. Loop to get the correct Email
        #     while True:
        #         speak(f"Tell me the email address for {name}.")
        #         speak("Say it like: john dot doe at gmail dot com")

        #         raw_email = take_command()
        #         if raw_email == "none": continue

        #         # Convert voice to email format
        #         email_address = parse_email_from_voice(raw_email)

        #         # 3. Confirm with user
        #         speak(f"I heard: {email_address}. Is this correct?")
        #         confirm = take_command()

        #         if "yes" in confirm or "correct" in confirm:
        #             save_new_email(name, email_address)
        #             speak(f"Saved {name}'s email successfully.")
        #             break # Exit the loop
        #         else:
        #             speak("Okay, let's try again.")

        # ... inside your while True loop ...

        if "english" in text or "english talkk" in text:
                if "text_to_learn" in text or "learn" in text or "learning mode" in text or "sikhna hai" in text or "chalo bt krte hain" in text or "bt krte hain" in text or "baat krna hai" in text:
                    Fast_DF_TTS.speak("ok sir, give me few time i am starting english learning mode")
                    from Features.english_tutor import start_english_learning_mode

                    # Pass the 'speak' function so the tutor can talk
                    # Note: Hum 'speak' function ko argument ki tarah bhej rahe hain
                    start_english_learning_mode(Fast_DF_TTS.speak)





        else:
            perform_browser_action(text)
            perform_youtube_action(text)

