import requests  
from win10toast import ToastNotifier
import time



import random



def alert(text):
    toaster = ToastNotifier()
    toaster.show_toast(
        "Jarvis",
        text,
        duration=1,
        icon_path=None,
        threaded=True
    )
    while toaster.notification_active():
        time.sleep(0.1)

def is_Online(url="https://www.google.com", timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return 200 <= response.status_code < 300
    except requests.ConnectionError:
        return False
    
    
    
