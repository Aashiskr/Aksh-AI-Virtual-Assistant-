import pyautogui as ui
import time
from Automation.open_App import open_App
from TextToSpeech import Fast_DF_TTS
import os
import re

# Helper to clean up time for searching (e.g., "9pm" -> "9:00 PM")
def normalize_time_for_search(time_str):
    # Remove dots and spaces to standardize (e.g., "9:00 p.m." -> "9:00pm")
    time_str = time_str.lower().replace(" ", "").replace(".", "")

    if "pm" in time_str:
        nums = time_str.replace("pm", "")
        period = "PM"
    elif "am" in time_str:
        nums = time_str.replace("am", "")
        period = "AM"
    else:
        return time_str # Return as is if unsure

    if ":" in nums:
        return f"{nums} {period}" # "9:30 PM"
    else:
        return f"{nums}:00 {period}" # "9:00 PM"

def find_meeting_by_time(spoken_time):
    """
    Searches meeting_schedule_data.txt for a line containing the time.
    Uses Regex to be flexible (matches 'p.m.', 'PM', 'pm', etc.)
    """
    file_path = "meeting_schedule_data.txt"
    if not os.path.exists(file_path):
        return None

    # 1. Get a standard format first: "12:00 PM"
    standard_time = normalize_time_for_search(spoken_time)
    print(f"Looking for standard time: {standard_time}")

    # 2. Split into components: "12:00" and "PM"
    try:
        target_time, target_period = standard_time.split()
    except ValueError:
        return None # Failed to split

    # 3. Create a flexible Regex Pattern
    # This pattern looks for "12:00" followed by "pm", "p.m.", "P.M.", or "PM"
    # \s* -> Matches zero or more spaces
    # p\.?m\.?  -> Matches 'p' followed by optional dot, 'm' followed by optional dot
    if target_period == "PM":
        period_regex = r"p\.?m\.?"
    else:
        period_regex = r"a\.?m\.?"

    # Final Regex: "12:00\s*p\.?m\.?"
    search_pattern = re.compile(f"{re.escape(target_time)}\\s*{period_regex}", re.IGNORECASE)

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Check if our flexible pattern exists in this line
                if search_pattern.search(line):
                    return line.strip()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return None

def send_specific_meeting(query):
    """
    Parses query like "send 9pm meeting link to aditya"
    """
    # 1. Extract the Name (Everything after 'to')
    if "to" in query:
        name = query.split("to")[-1].strip()
        # Remove any trailing punctuation
        name = name.replace(".", "").strip()
    else:
        Fast_DF_TTS.speak("I didn't hear a name. Please say 'send to Name'.")
        return

    # 2. Extract the Time
    time_regex = r'(\d{1,2}(?::\d{2})?\s?(?:am|pm|a\.m\.|p\.m\.))'
    match = re.search(time_regex, query, re.IGNORECASE)

    if not match:
        Fast_DF_TTS.speak("I couldn't find a time in your command.")
        return

    spoken_time = match.group(0)
    print(f"Detected time input: {spoken_time}")

    # 3. Find the meeting in the file
    meeting_details = find_meeting_by_time(spoken_time)

    if not meeting_details:
        clean_time = normalize_time_for_search(spoken_time)
        Fast_DF_TTS.speak(f"Sorry, I couldn't find any meeting scheduled for {clean_time}.")
        return

    # 4. Send the Message
    Fast_DF_TTS.speak(f"Found it. Sending to {name}.")

    open_App("whatsapp")
    time.sleep(2)

    # Search Contact
    ui.leftClick(x=450, y=150)
    time.sleep(1)
    ui.write(name)
    time.sleep(2)
    ui.leftClick(x=450, y=200)
    time.sleep(1)

    # Type Message
    ui.leftClick(x=1000, y=1000)
    time.sleep(1)
    ui.write(f"Here is the meeting link you asked for: {meeting_details}")
    time.sleep(1)
    ui.press('enter')

    Fast_DF_TTS.speak("Sent successfully.")
