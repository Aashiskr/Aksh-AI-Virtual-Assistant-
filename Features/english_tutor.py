import google.generativeai as genai
import speech_recognition as sr
import os

# --- CONFIGURATION ---
# Make sure your API Key is pasted here!
API_KEY = "AIzaSyCraEKQBqttpLcnXkAuozBHPlR1SBXojcI"

# AI Setup
genai.configure(api_key=API_KEY)# type: ignore

def get_best_model():
    """
    Automatically searches for a working Gemini model
    instead of guessing the name.
    """
    try:
        print("Searching for available AI models...")
        for m in genai.list_models():# type: ignore
            if 'generateContent' in m.supported_generation_methods:
                # Prefer Flash for speed
                if 'flash' in m.name:
                    print(f"Selected Model: {m.name}")
                    return genai.GenerativeModel(m.name)# type: ignore

        # If no Flash, find any Gemini model
        for m in genai.list_models():# type: ignore
            if 'generateContent' in m.supported_generation_methods and 'gemini' in m.name:
                print(f"Selected Model: {m.name}")
                return genai.GenerativeModel(m.name)# type: ignore

    except Exception as e:
        print(f"Error listing models: {e}")

    # Absolute fallback if listing fails
    return genai.GenerativeModel('gemini-pro')# type: ignore

def listen_english():
    """
    Specially tuned listener for English conversation.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening (English Mode)...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            # Listen for input
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            query = r.recognize_google(audio, language='en-US') # type: ignore
            print(f"You said: {query}")
            return query
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except Exception as e:
            print(f"Mic Error: {e}")
            return None

def start_english_learning_mode(speak_func):
    """
    Starts the continuous conversation loop.
    """
    # 1. Auto-Select Model
    model = get_best_model()

    speak_func("English learning mode activated.")
    speak_func("I am ready. What topic should we discuss?")

    # 2. Start Chat Session
    try:
        chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["Act as an English Tutor. I will speak to you in English. "
                          "Check my grammar strictly. "
                          "If my sentence is WRONG: Say 'Correction: <Correct Sentence>', and then reply. "
                          "If my sentence is CORRECT: Say 'Your sentence is correct.', and then reply. "
                          "Keep replies short (max 2 sentences)."]
            },
            {
                "role": "model",
                "parts": ["Understood. I am ready to help you practice English. What is our topic?"]
            }
        ])
    except Exception as e:
        print(f"Chat Init Error: {e}")
        speak_func("I could not connect to the AI brain. Please check your API Key.")
        return

    while True:
        # 3. Listen
        user_text = listen_english()

        if not user_text:
            continue

        # 4. Exit Logic
        if "exit" in user_text.lower() or "stop" in user_text.lower() or "normal mode" in user_text.lower():
            speak_func("Exiting English learning mode.")
            break

        # 5. Send to AI
        try:
            response = chat.send_message(user_text)
            reply = response.text

            print(f"Aksh: {reply}")
            speak_func(reply)

        except Exception as e:
            # Print the REAL error to the console so we can debug
            print(f"API Error: {e}")
            speak_func("I lost the connection. Please say that again.")
