import datetime
import random
import pywhatkit

def play_time_aware_content():
    # 1. Get current hour (0 to 24)
    current_hour = datetime.datetime.now().hour

    # 2. Define Time Slots & Content

    # MORNING (5 AM to 12 PM) -> Spiritual / News / Motivation
    morning_picks = [
        "latest india news live english",
        "morning bhajans hindi",
        "positive affirmations for success",
        "morning workout music",
        "surya namaskar mantra"
    ]

    # AFTERNOON (12 PM to 5 PM) -> Work / Focus / Lofi
    afternoon_picks = [
        "lofi hip hop radio - beats to relax/study to",
        "soft bollywood acoustic songs",
        "instrumental background music for work",
        "ted talk productivity",
        "arijit singh slow songs"
    ]

    # EVENING (5 PM to 9 PM) -> Fun / Trending / Snacks
    evening_picks = [
        "latest punjabi party songs",
        "trending bollywood songs 2024",
        "standup comedy hindi",
        "coke studio india best songs",
        "evening coffee jazz music"
    ]

    # NIGHT (9 PM to 5 AM) -> Sleep / Relax / Old Classics
    night_picks = [
        "guided sleep meditation 10 minutes",
        "old hindi songs kishore kumar",
        "slowed and reverb hindi songs",
        "rain sounds for sleeping black screen",
        "ghazals jagjit singh"
    ]

    # 3. DECIDE WHAT TO PLAY
    if 5 <= current_hour < 12:
        category = "Morning"
        song = random.choice(morning_picks)
        message = "Good Morning! Here is something to start your day."

    elif 12 <= current_hour < 17:
        category = "Afternoon"
        song = random.choice(afternoon_picks)
        message = "Good Afternoon. Keeping the vibes focused and chill."

    elif 17 <= current_hour < 21:
        category = "Evening"
        song = random.choice(evening_picks)
        message = "Good Evening! Let's energize the mood."

    else: # 9 PM to 5 AM
        category = "Night"
        song = random.choice(night_picks)
        message = "It's late. Playing something relaxing for you."

    print(f"⏰ Time: {current_hour}:00 | Category: {category}")
    print(f"🎵 Playing: {song}")

    # 4. EXECUTE
    pywhatkit.playonyt(song) # type: ignore
    return message
