import threading
from internet_check import is_Online
from Alert import Alert
from Data.DLG_Data import online_dlg,please_online_first_dlg
import random
from co_brain import aksh
from TextToSpeech.Fast_DF_TTS import speak
import os 
from Automation.Battery import check_plug,battery_Alert
from Time_Operations.brain import input_manage
from Time_Operations.throw_alert import check_schedule,check_Alam

rand_offline_dlg = random.choice(please_online_first_dlg)
rand_online_dlg = random.choice(online_dlg)

file_path = r'C:\Users\Ashish Kumar\OneDrive\Desktop\Aksh\schedule.txt'
Alam_path = r'C:\Users\Ashish Kumar\OneDrive\Desktop\Aksh\Alam_data.txt'

def main():
    if is_Online():
        t1 = threading.Thread(target=speak,args=(rand_online_dlg,))
        t2 = threading.Thread(target=Alert,args=(rand_online_dlg,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        t3 = threading.Thread(target=check_plug)
        t4 = threading.Thread(target=battery_Alert)
        t5 = threading.Thread(target=aksh)
        t6 = threading.Thread(target=check_schedule,args=(file_path,))
        t7 = threading.Thread(target=check_Alam,args=(Alam_path,))
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
    else:
        Alert(rand_offline_dlg)
        

main()
