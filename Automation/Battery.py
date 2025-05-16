import psutil
import time
from TextToSpeech.Fast_DF_TTS import speak
import threading
from Alert import Alert

battery = psutil.sensors_battery()

def battery_Alert():
    while True:
        time.sleep(3)
        percentage = int(battery.percent)
        if percentage == 100 and battery.power_plugged:
            t1 = threading.Thread(target=Alert,args=("100% charge unplug it",))
            t2 = threading.Thread(target=speak,args=("100 percent charged please unplug it.",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            # alert100()
            # speak("100% charged. Please unplug it.")
        if percentage <= 20:
            t1 = threading.Thread(target=Alert,args=("Battery Low",))
            t2 = threading.Thread(target=speak,args=("Sir, Sorry to intrupt you but battery is low now",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            time.sleep(100)

        if percentage <= 10 and battery.not_plugged:
            t1 = threading.Thread(target=Alert,args=("Battery is too Low",))
            t2 = threading.Thread(target=speak,args=("Sir, Sorry to intrupt you but battery is very low now 10 percent less",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()

        if percentage <= 5:
            t1 = threading.Thread(target=Alert,args=("Battery is going to died",))
            t2 = threading.Thread(target=speak,args=("Sir, Sorry to intrupt you but your battery 5 charge your system now",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()

        time.sleep(10)  # Sleep for a short duration to avoid excessive CPU usage


def check_plug():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                t1 = threading.Thread(target=Alert, args=("Charging **STARTED**",))
                t2 = threading.Thread(target=speak, args=("Sir, your system is plugged in now",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
            else:
                t1 = threading.Thread(target=Alert, args=("Unplugged",))
                t2 = threading.Thread(target=speak, args=("Sir, your system is unplugged now",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()

            previous_state = battery.power_plugged  

def check_percentage():
    battery = psutil.sensors_battery()
    if battery is None:
        print("Battery information not available.")
        return

    percent = int(battery.percent)
    t1 = threading.Thread(target=Alert,args=(f"The device is running on {percent} % power",))
    t2 = threading.Thread(target=speak,args=(f"The device is running on {percent} % power",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

