import pygetwindow as gw
import pyautogui
import time
import ctypes

# Windows API Constants for forcing focus
SW_RESTORE = 9
user32 = ctypes.windll.user32

def switch_to_app(app_name):
    """
    Robust window switcher that handles speech errors and forces focus.
    """
    # 1. Speech Cleaning & Aliases (Fixes "TVS Code", "Chromepp" etc.)
    target = app_name.lower().strip()

    # Dictionary: { "what user says": "what window title actually has" }
    aliases = {
        "code": "visual studio code",
        "vs code": "visual studio code",
        "tvs": "visual studio code",  # Fix for "TVS code" error
        "brave": "brave",
        "chrome": "chrome",
        "whatsapp": "whatsapp",
        "notepad": "notepad",
        "terminal": "powershell",
    }

    # Check if the user used a short name (like "Code") and swap it for the full name
    for key in aliases:
        if key in target:
            target = aliases[key]
            break

    if not target: return False

    print(f"Searching for window matching: '{target}'")

    # 2. Get all windows
    windows = gw.getAllWindows()
    found_window = None

    for w in windows:
        if w.title and target in w.title.lower():
            found_window = w
            break

    if found_window:
        try:
            print(f"Attempting switch to: {found_window.title}")

            # 3. FORCE SHOW (Direct Windows API)
            # If it's minimized, this forces it open using the OS handle
            if found_window.isMinimized:
                user32.ShowWindow(found_window._hWnd, SW_RESTORE)
                time.sleep(0.2)

            # 4. The "Alt Key" Hack (Still needed for Focus)
            # Pressing Alt tells Windows "User is active, allow window switch"
            pyautogui.press('alt')

            # 5. Activate
            found_window.activate()

            # 6. Extra safety: Move mouse slightly to wake UI
            pyautogui.moveRel(1, 0)

            return True

        except Exception as e:
            msg = str(e)
            if "Error code from Windows: 0" in msg:
                return True
            print(f"Switch Error: {msg}")
            return False

    print(f"Could not find any open window named '{app_name}' (Target: {target})")
    return False
