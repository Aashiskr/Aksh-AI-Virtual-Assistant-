from gtts import gTTS
from playsound import playsound
import os

def speak2(message: str, lang: str = 'hi', file_name: str = "output.mp3"):
    try:
        tts = gTTS(text=message, lang=lang, slow=False)
        tts.save(file_name)
        playsound(file_name)
        os.remove(file_name)
    except Exception as e:
        print("Error:", e)
