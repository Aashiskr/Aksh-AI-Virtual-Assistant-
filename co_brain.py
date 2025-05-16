from Automation.Automation_Brain import Auto_main_brain,clear_file
from inf_STT import listen
from TextToSpeech.Fast_DF_TTS import speak
import threading 
import time
from os import getcwd
from Time_Operations.brain import input_manage,input_manage_Alarm

numbers = ["1:","2:","3:","4:","5:","6:","7:","8:","9:"]

def clear_file():
    with open(f"{getcwd()}\\input.txt","w")as file:
            file.truncate(0)

from Data.DLG_Data import online_dlg,please_online_first_dlg
import random
from Automation.Battery import battery_Alert,check_percentage,check_plug

rand_offline_dlg = random.choice(please_online_first_dlg)
rand_online_dlg = random.choice(online_dlg)

def check_inputs():
    output_text = ""
    while True:
        with open("input.txt","r")as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text.startswith("remind me"):
                output_text = output_text.replace("p.m.","PM")
                output_text = output_text.replace("a.m.","AM")
                if "11:" in output_text or "12:" in output_text:
                    input_manage(output_text) 
                    speak("Done Sir ! I will remind you")
                    clear_file()
                else:
                    for number in numbers:
                        if number in output_text:
                            output_text = output_text.replace(number,f"0{number}")
                            input_manage(output_text) 
                            speak("Done Sir ! I will remind you")
                            clear_file()
            elif output_text.startswith("set alarm"):
                output_text = output_text.replace("p.m.","PM")
                output_text = output_text.replace("a.m.","AM")
                if "11:" in output_text or "12:" in output_text:
                    input_manage_Alarm(output_text) 
                    speak("Done Sir ! Your Alarm is all set to remind you") 
                    clear_file()
                else:
                    for number in numbers:
                        if number in output_text:
                            output_text = output_text.replace(number,f"0{number}")
                            input_manage_Alarm(output_text) 
                            speak("Done Sir ! Your Alarm is all set to remind you")
                            clear_file()
            else:
                Auto_main_brain(output_text)

def aksh():
    clear_file() 
    t1 = threading.Thread( target = listen )
    t2 = threading.Thread( target = check_inputs ) 
    t1.start()
    t2.start()
    t1.join()
    t2.join()


