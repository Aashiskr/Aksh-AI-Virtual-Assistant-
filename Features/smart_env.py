import time
import datetime
import psutil
import screen_brightness_control as sbc
import pyautogui
import pythoncom # Keeps the thread safe

# Speed up the keyboard presses for volume
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.02

def set_system_volume(level):
    """
    Sets volume by pressing keyboard keys.
    Reliable and Visual (Judges see the slider move).
    """
    try:
        # 1. Mute first to ensure we start from 0 (Optional, but safer)
        # pyautogui.press('volumemute')

        # 2. Reset to 0 (Press Down 50 times - Covers 100%)
        pyautogui.press('volumedown', presses=50)

        # 3. Increase to desired level (Each press is usually 2%)
        # For 10%, we need 5 presses (5 * 2 = 10)
        # For 100%, we need 50 presses
        presses_needed = int(level / 2)
        pyautogui.press('volumeup', presses=presses_needed)

        print(f"🔊 Volume set to approx {level}%")

    except Exception as e:
        print(f"❌ Error setting volume: {e}")

def start_monitoring():
    print("👀 Smart Environment Monitor Started...")

    # Initialize Windows COM for this thread (Fixes brightness crashes)
    pythoncom.CoInitialize()

    is_whatsapp_mode = False
    is_night_mode = False

    while True:
        try:
            # --- 1. CHECK WHATSAPP (Volume Logic) ---
            # We fetch process list safely
            process_names = [p.name() for p in psutil.process_iter()]

            if "WhatsApp.exe" in process_names:
                if not is_whatsapp_mode:
                    print("detected WhatsApp! Lowering volume to 10%...")
                    set_system_volume(10)
                    is_whatsapp_mode = True
            else:
                if is_whatsapp_mode:
                    print("WhatsApp closed. Restoring volume to 100%...")
                    set_system_volume(100)
                    is_whatsapp_mode = False

            # --- 2. CHECK TIME (Night Light Logic) ---
            current_hour = datetime.datetime.now().hour

            # NIGHT MODE: 7 PM (19) to 6 AM (6)
            if current_hour >= 19 or current_hour < 6:
                if not is_night_mode:
                    print("🌙 It's Night Time! Lowering Brightness...")
                    try:
                        sbc.set_brightness(20)
                    except:
                        pass
                    is_night_mode = True
            else:
                if is_night_mode:
                    print("☀️ It's Day Time! Increasing Brightness...")
                    try:
                        sbc.set_brightness(100)
                    except:
                        pass
                    is_night_mode = False

            # Sleep for 2 seconds to save CPU
            time.sleep(2)

        except Exception as e:
            print(f"Monitor Loop Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    start_monitoring()
