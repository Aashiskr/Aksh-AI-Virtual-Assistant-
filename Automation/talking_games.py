import random
from TextToSpeech import Fast_DF_TTS
from Data.DLG_Data import kbc_questions  
from os import getcwd
import time

def clear_file():
    with open(f"{getcwd()}\\input.txt","w")as file:
            file.truncate(0)

def wait_for_input():
    output_text = ""
    while True:
        with open("input.txt", "r") as file:
            input_text = file.read().lower().strip()
        if input_text != output_text and input_text:
            return input_text

def talking_games():
    Fast_DF_TTS.speak("Great! We have two talking games: Guess the Number or KBC quiz.")
    Fast_DF_TTS.speak("Say 'number game' to guess a number or 'KBC Game' to play the quiz.")
    
    clear_file()
    choice = wait_for_input()

    if "number game" in choice:
        Fast_DF_TTS.speak("Think of a number. Don't tell me! I will try to guess it.")
        number = random.randint(1, 10)
    
        Fast_DF_TTS.speak("Double it. Just say 'okay' when you're done.")
        time.sleep(1.5)
    
        Fast_DF_TTS.speak(f"Now add {number} to it.")
        time.sleep(1.5)
        
        Fast_DF_TTS.speak("Now divide the result by 2.")
        time.sleep(1.5)
        
        Fast_DF_TTS.speak("Now subtract the number you thought of at the beginning.")
        time.sleep(1.5)
        
        Fast_DF_TTS.speak("Say 'done' when you're finished.")
        time.sleep(1.5)
        
        Fast_DF_TTS.speak(f"The number in your mind is {number / 2}, right?")
        time.sleep(1.5)
        
        clear_file()


    elif "kbc game" in choice:
        Fast_DF_TTS.speak("Welcome to KBC! Let's begin.")
        score = 0
        for i, q in enumerate(kbc_questions, start=1):
            Fast_DF_TTS.speak(f"Question {i}: {q['question']}")
            for opt in q["options"]:
                Fast_DF_TTS.speak(opt)
            time.sleep(1)
            clear_file()
            answer = wait_for_input()
            if answer.strip().lower() == q["answer"].strip().lower():
                Fast_DF_TTS.speak("Correct answer!")
                score += 1
            elif answer.strip().lower() == "exit" or answer.strip().lower() == "quit":
                Fast_DF_TTS.speak("Exiting the game. Goodbye!")
                break
            else:
                Fast_DF_TTS.speak(f"Wrong answer. The correct answer was option {q['answer'].upper()}.")
        Fast_DF_TTS.speak(f"You scored {score} out of {len(kbc_questions)} in the KBC game.")

    else:
        Fast_DF_TTS.speak("Sorry, I didn't understand. Please try again and choose a valid game.")
