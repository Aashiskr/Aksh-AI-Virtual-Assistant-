from open_App import open_App
from Web_open import openweb
import pyautogui as gui
from time import sleep

def close():
    gui.hotkey('alt', 'f4')

def Open_Brain(text):
    if "website" in text or "open website name" in text:
        text = text.replace("open", "").strip()
        text = text.replace("website", "").strip()
        text = text.replace("open website name", "").strip()
        openweb(text)
        
    else:
        text = text.replace("app", "").strip()
        text = text.replace("open", "").strip()
        open_App(text)
        





while True:
    x = input("What do you want to open: ")
    Open_Brain(x)