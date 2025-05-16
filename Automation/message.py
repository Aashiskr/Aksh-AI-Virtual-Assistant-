import webbrowser
import pyautogui as ui
import time
from Automation.open_App import open_App
from TextToSpeech import Fast_DF_TTS
from os import getcwd

def clear_file():
    with open(f"{getcwd()}\\input.txt","w")as file:
            file.truncate(0)


def message_the_person(text):
    open_App("whatsapp")
    time.sleep(1)

    ui.leftClick(x=450, y=150)  # Click into the search box
    time.sleep(1)
    ui.write(text)
    time.sleep(1)
    ui.leftClick(x=450, y=200)  # Click on the contact
    time.sleep(1)
    ui.leftClick(x=1000, y=1000)  # Click on the message box
    time.sleep(1)

    while True:
        Fast_DF_TTS.speak("Tell me the message you want to send")
        time.sleep(1)
        clear_file()

        # Wait for user to enter the message
        output_text = ""
        while True:
            with open("input.txt", "r") as file:
                input_text = file.read().lower()
            if input_text != output_text:
                output_text = input_text
                if output_text:
                    break

        ui.write(output_text)
        time.sleep(1)
        ui.press('enter')
        time.sleep(1)

        Fast_DF_TTS.speak("Do you want to send more messages?")
        time.sleep(2.5)
        clear_file()

        # Wait for user response
        response = ""
        while True:
            with open("input.txt", "r") as file:
                new_response = file.read().lower()
            if new_response != response:
                response = new_response
                if response:
                    break

        if "mt kro message" in response or "stop message" in response or "stop messaging" in response or "stop" in response or "no" in response or "no close the tab" in response or "no close" in response or "no close the tab" in response or "no close the tab" in response:
            Fast_DF_TTS.speak("Okay, message sending stopped.")
            break

    

    
