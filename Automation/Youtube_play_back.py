import pyautogui as gui
import time

# === YouTube Control Functions ===

def youtube_play_pause():
    """Toggle play/pause."""
    gui.press('k')
    time.sleep(0.1)

def youtube_mute_unmute():
    """Mute or unmute audio."""
    gui.press('m')
    time.sleep(0.1)

def youtube_volume_up():
    """Increase volume."""
    gui.press('up')
    time.sleep(0.1)

def youtube_volume_down():
    """Decrease volume."""
    gui.press('down')
    time.sleep(0.1)

def youtube_forward():
    """Skip forward 10 seconds."""
    gui.press('l')
    time.sleep(0.1)

def youtube_backward():
    """Rewind 10 seconds."""
    gui.press('j')
    time.sleep(0.1)

def youtube_fullscreen():
    """Toggle fullscreen mode."""
    gui.press('f')
    time.sleep(0.1)

def youtube_miniplayer():
    """Toggle miniplayer mode."""
    gui.press('i')
    time.sleep(0.1)

def youtube_theater_mode():
    """Toggle theater mode."""
    gui.press('t')
    time.sleep(0.1)

def youtube_next_video():
    """Go to the next video."""
    gui.hotkey('shift', 'n')
    time.sleep(0.1)

def youtube_previous_video():
    """Go to the previous video."""
    gui.hotkey('shift', 'p')
    time.sleep(0.1)

def youtube_captions():
    """Toggle subtitles/captions."""
    gui.press('c')
    time.sleep(0.1)

def youtube_home():
    """Go to the beginning of the video."""
    gui.press('0')
    time.sleep(0.1)

def youtube_toggle_playback_speed():
    """YouTube does not have a default shortcut for this, unless custom."""
    print("Playback speed control not supported via default shortcut.")

# === Dispatcher Function ===

def perform_youtube_action(command: str):
    command = command.lower()

    if "play" in command or "pause" in command:
        youtube_play_pause()
    elif "mute" in command or "unmute" in command:
        youtube_mute_unmute()
    elif "volume up" in command:
        youtube_volume_up()
    elif "volume down" in command:
        youtube_volume_down()
    elif "forward" in command or "skip" in command:
        youtube_forward()
    elif "backward" in command or "rewind" in command:
        youtube_backward()
    elif "fullscreen" in command:
        youtube_fullscreen()
    elif "miniplayer" in command:
        youtube_miniplayer()
    elif "theater" in command:
        youtube_theater_mode()
    elif "next video" in command:
        youtube_next_video()
    elif "previous video" in command:
        youtube_previous_video()
    elif "captions" in command or "subtitles" in command:
        youtube_captions()
    elif "home" in command:
        youtube_home()
    else:
        pass
