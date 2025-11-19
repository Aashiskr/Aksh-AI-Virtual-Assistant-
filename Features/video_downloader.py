import yt_dlp
import pyautogui
import pyperclip
import time
import os

def get_active_url():
    try:
        # 1. Focus on the address bar (Alt + D is a standard shortcut for browsers)
        pyautogui.hotkey('alt', 'd')
        time.sleep(0.1) # Small delay to ensure focus

        # 2. Copy the text (Ctrl + C)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1) # Wait for copy

        # 3. Get the URL from the clipboard
        url = pyperclip.paste()

        # 4. Click/Press Esc to defocus address bar so you can keep watching
        pyautogui.press('esc')

        return url
    except Exception as e:
        print(f"Error grabbing URL: {e}")
        return None

def download_video(url, save_path):
    """
    Downloads video using yt-dlp.
    """
    if not url.startswith("http"):
        return None

    # Define download options
    ydl_opts = {
        'format': 'best',
        # FIXED LINE BELOW: Uses the save_path variable properly
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore
            info = ydl.extract_info(url, download=True)
            return info.get('title', 'video')
    except Exception as e:
        print(f"Download failed: {e}")
        return None

# Main function to be called by your assistant
def download_current_video():
    # 1. Get URL
    url = get_active_url()
    print(f"Detected URL: {url}")

    if url:
        # 2. Set download folder
        # We define your specific path here using r"" (Raw string) to handle backslashes
        download_folder = r"C:\Users\ar685\Downloads"

        # Create the folder if it doesn't exist (just in case)
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # 3. Start Download
        # We pass the folder to the function above
        title = download_video(url, download_folder)
        return title
    return None
