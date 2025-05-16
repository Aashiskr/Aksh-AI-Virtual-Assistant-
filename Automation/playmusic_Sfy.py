import webbrowser
import pyautogui as ui
import time

def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(6)  # Wait for the page

    # You can manually position your browser so search box is in a known location
    ui.leftClick(x=850, y=150) 
    time.sleep(1.5)
    ui.write(song_name)
    time.sleep(3)
    ui.leftClick(x=550,y=580) #1050 1000


