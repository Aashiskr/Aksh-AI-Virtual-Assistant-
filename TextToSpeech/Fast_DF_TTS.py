import requests
from playsound import playsound
import os
from typing import Union

def generate_audio(message: str, voice: str = "Matthew"):
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        result = requests.get(url=url, headers=headers)
        return result.content
    except:
        return None

def speak(message: str, voice: str = "Matthew", folder: str = "", extension: str = ".mp3") -> Union[None, str]:
    try:
        result_content = generate_audio(message, voice)
        
        file_path = os.path.join(folder, f"{voice}{extension}")

        with open(file_path, "wb") as file:
            file.write(result_content)

        playsound(file_path)
        os.remove(file_path)

        return None

    except Exception as e:
        print(e)
