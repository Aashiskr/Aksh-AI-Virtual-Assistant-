import os
import subprocess
import tempfile
from playsound import playsound
import threading

def speak(text: str, voice: str = "hi-IN-SwaraNeural") -> None: # hi-IN-MadhurNeural , hi-IN-AditiNeural , en-CA-LiamNeural ,hi-IN-SwaraNeural;
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            output_file = tmpfile.name

        command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "{output_file}"'
        subprocess.run(command, shell=True, check=True)

        def play_and_cleanup(path):
            try:
                playsound(path)
            finally:
                os.remove(path)

        threading.Thread(target=play_and_cleanup, args=(output_file,)).start()

    except Exception as e:
        print("Error:", e)

# Loop for user input
if __name__ == "__main__":
    while True:
        x = input("You: ")
        if x.lower() in ["exit", "quit", "stop"]:
            break
        speak(x)
