import os

from winotify import Notification, audio
from os import getcwd

def Alert(text):
    icon_path = fr"{getcwd()}\logo.jpg"

    toast = Notification(
        app_id="Aksh",
        title=text,
        duration="short",
        icon=icon_path 
    )



    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Click Me",launch="https://www.google.com")
    toast.add_actions(label="Dismiss",launch="about:blank")

    toast.show()

