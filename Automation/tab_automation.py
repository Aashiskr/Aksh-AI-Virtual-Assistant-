import pyautogui as gui
import time

def open_new_tab():
    gui.hotkey('ctrl', 't')
    time.sleep(1)

def close_current_tab():
    gui.hotkey('ctrl', 'w')
    time.sleep(1)

def open_browser_menu():
    gui.hotkey('ctrl', 'f')  
    time.sleep(1)

def zoom_in():
    gui.hotkey('ctrl', '+')
    time.sleep(1)

def zoom_out():
    gui.hotkey('ctrl', '-')
    time.sleep(1)

def go_forward():
    gui.hotkey('alt', 'right')
    time.sleep(1)

def go_back():
    gui.hotkey('alt', 'left')
    time.sleep(1)

def open_dev_tools():
    gui.hotkey('ctrl', 'shift', 'i')

def toggle_fullscreen():
    gui.hotkey('f11')

def open_bookmark():
    gui.hotkey('ctrl', 'b')
    time.sleep(1)

def open_history():
    gui.hotkey('ctrl', 'h')
    time.sleep(1)

def switch_to_previous_tab():
    gui.hotkey('ctrl', 'shift', 'tab')

def switch_to_next_tab():
    gui.hotkey('ctrl', 'tab')

def refresh_page():
    gui.hotkey('ctrl', 'r')

def scroll_down():
    gui.scroll(-500)  # You can adjust the value based on how fast you want to scroll
    time.sleep(1)

def scroll_up():
    gui.scroll(500)
    time.sleep(1)

def click_at_cursor():
    gui.click()

def move_cursor_right(pixels=100):
    x, y = gui.position()
    gui.moveTo(x + pixels, y)

def move_cursor_left(pixels=100):
    x, y = gui.position()
    gui.moveTo(x - pixels, y)

def open_private_window():
    gui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)

def perform_browser_action(text):
    text = text.lower()
    gui.moveTo(x=800, y=600)

    if "new tab" in text or "new tab kholo" in text:
        open_new_tab()
    elif "close tab" in text or "tab band karo" in text or "tab close" in text or "close the tab" in text or "close this tab" in text:
        close_current_tab()
    elif "find" in text or "search" in text:
        open_browser_menu()
    elif "zoom in" in text or "bada karo" in text:
        zoom_in()
    elif "zoom out" in text or "chhota karo" in text:
        zoom_out()
    elif "forward" in text or "aage jao" in text:
        go_forward()
    elif "back" in text or "peeche jao" in text:
        go_back()
    elif "dev tools" in text or "developer tools" in text:
        open_dev_tools()
    elif "full screen" in text or "poora screen" in text:
        toggle_fullscreen()
    elif "bookmark on" in text or "bookmarks kholo" in text:
        open_bookmark()
    elif "histry kholo" in text or "history kholo" in text:
        open_history()
    elif "previous tab" in text or "pichla tab" in text:
        switch_to_previous_tab()
    elif "next tab" in text or "agla tab" in text:
        switch_to_next_tab()
    elif "refresh page" in text or "page reload" in text:
        refresh_page()
    elif "scroll down" in text or "neeche jao" in text:
        scroll_down()
    elif "scroll down again" in text or "neeche jao firse" in text:
        scroll_down()
    elif "scroll up" in text or "upar jao" in text:
        scroll_up()
    elif "scroll up" in text or "upar jao firse" in text:
        scroll_up()
    elif "click here" in text or "click karo" in text:
        click_at_cursor()

    elif "move right" in text or "daaye jao" in text:
        move_cursor_right()
    elif "move left" in text or "baaye jao" in text:
        move_cursor_left()
    elif "move right again" in text or "daaye jao firse" in text:
        move_cursor_right()
    elif "move left again" in text or "baaye jao firse" in text:
        move_cursor_left()
    if "private window" in text or "naya private window" in text:
        open_private_window()
    else:
        pass


