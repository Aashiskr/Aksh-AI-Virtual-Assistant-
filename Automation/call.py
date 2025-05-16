import webbrowser
import pyautogui as ui
import time
from Automation.open_App import open_App


def call_the_person(text):
    open_App("whatsapp")
    time.sleep(3)  # Wait for the page

    # You can manually position your browser so search box is in a known location
    ui.leftClick(x=450, y=150)  # Click into the search box 500
    time.sleep(1)
    ui.write(text)
    time.sleep(3)
    ui.leftClick(x=450, y=200)
    time.sleep(0.5)
    ui.leftClick(x=1800, y=100)  # Click on the call button
    
