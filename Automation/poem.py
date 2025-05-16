from TextToSpeech import Fast_DF_TTS
from os import getcwd

def clear_file():
    with open(f"{getcwd()}\\input.txt","w")as file:
            file.truncate(0)

import random
import time

def play_poem():
    # List of poems
    poems = [
        "Johny Johny,\nYes, Papa?\nEating sugar?\nNo, Papa.\nTelling lies?\nNo, Papa.\nOpen your mouth!\nHa ha ha!"
        "Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you.",
        "The road goes ever on and on,\nDown from the door where it began.\nNow far ahead the road has gone,\nAnd I must follow if I can.",
        "In the middle of the journey,\nI found a path so bright,\nWith every step I take,\nI feel the world's delight."
    ]
    
    # Randomly select a poem
    selected_poem = random.choice(poems)
    
    # Speak the poem
    Fast_DF_TTS.speak("Here is a poem for you")
    time.sleep(2)
    Fast_DF_TTS.speak(selected_poem)