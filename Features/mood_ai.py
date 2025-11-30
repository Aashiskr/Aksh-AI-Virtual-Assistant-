import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pywhatkit

# 1. MUSIC PLAYLISTS (Different search terms for variety)
happy_songs = [
    "latest bollywood party songs 2024",
    "punjabi high energy dance mix",
    "best upbeat hindi songs",
    "top 50 happy mood songs india",
    "badshah party hits"
]

sad_songs = [
    "arijit singh sad songs lofi",
    "best emotional hindi songs",
    "motivational songs for hard times hindi",
    "soothing piano music for sad mood",
    "kk sad songs collection"
]

angry_songs = [
    "10 minute meditation for anger",
    "calming flute music for relaxation",
    "deep breathing relaxation music",
    "stress relief nature sounds"
]

# 2. TRAINING DATA (Same as before)
data = [
    ("I am feeling very sad today", "sad"),
    ("I feel depressed and lonely", "sad"),
    ("I am not feeling good", "sad"),
    ("I want to cry", "sad"),
    ("My mood is off", "sad"),
    ("I am feeling amazing", "happy"),
    ("I am so happy today", "happy"),
    ("What a beautiful day", "happy"),
    ("I feel great", "happy"),
    ("I am excited", "happy"),
    ("I am very angry", "angry"),
    ("I hate this situation", "angry"),
    ("I am furious right now", "angry"),
    ("This is annoying", "angry")
]

sentences, labels = zip(*data)

# 3. BUILD MODEL
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(sentences, labels)

# 4. SMART FUNCTION
def detect_and_respond(user_text):
    prediction = model.predict([user_text])[0]
    print(f"🧠 AI Detected Mood: {prediction.upper()}") # type: ignore

    if prediction == "sad":
        # Pick a RANDOM song from the sad list
        song = random.choice(sad_songs)
        print(f"Playing: {song}")
        pywhatkit.playonyt(song) # type: ignore
        return "Don't worry, everything will be fine. Playing something to cheer you up."

    elif prediction == "happy":
        song = random.choice(happy_songs)
        print(f"Playing: {song}")
        pywhatkit.playonyt(song) # type: ignore
        return "Awesome! Let's keep the party going."

    elif prediction == "angry":
        song = random.choice(angry_songs)
        print(f"Playing: {song}")
        pywhatkit.playonyt(song) # type: ignore
        return "I sense some tension. Let's take a moment to relax."

    else:
        return "I am listening."
