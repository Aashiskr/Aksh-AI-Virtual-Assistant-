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

def close():
    gui.hotkey('alt', 'f4')

def search_google(text):
    pywhatkit.search(text)

def kill_program():
    gui.hotkey('ctrl', 'C')

def tab_close():
    gui.hotkey('ctrl','w')

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

        if "check battery percentage" in text or "check battery level" in text:
            check_percentage()

        if "call someone" in text or "i want to call" in text:
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
        if "message someone" in text or "i want to message" in text or "send message" in text:
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
        
        if "check internet speed" in text or "check internet speed" in text:
            Fast_DF_TTS.speak("Checking internet speed")
            time.sleep(2)
            speed = get_internet_speed()
            Fast_DF_TTS.speak(f"Your internet speed is {speed} Mbps")

        if "hello aksh" in text or "hi aksh" in text or "hey aksh" in text or "hello" in text or "hi" in text or "hey" in text:
            Fast_DF_TTS.speak("Hello sir, how can I help you?")
            time.sleep(1)
            clear_file()

        if "shut down computer" in text or "shutdown this pc" in text or "turn off this device" in text:
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

        else:
            perform_browser_action(text)
            perform_youtube_action(text)

