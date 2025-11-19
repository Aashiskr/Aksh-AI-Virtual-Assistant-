import pyautogui as gui
import time

import ctypes

import pyautogui as ui

# Ye fail-safe off karta hai taki agar mouse corner me jaye to program crash na ho
ui.FAILSAFE = False

def move_cursor_right(pixels=100):
    # x=pixels, y=0 (Sirf right jana hai, upar/niche nahi)
    ui.moveRel(pixels, 0, duration=0.2)

def move_cursor_left(pixels=100):
    # x=-pixels (Left jane ke liye minus)
    ui.moveRel(-pixels, 0, duration=0.2)

def move_cursor_up(pixels=100):
    # y=-pixels (Upar jane ke liye minus)
    ui.moveRel(0, -pixels, duration=0.2)

def move_cursor_down(pixels=100):
    # y=pixels (Niche jane ke liye plus)
    ui.moveRel(0, pixels, duration=0.2)

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


def open_private_window():
    gui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)

def perform_browser_action(text):
    text = text.lower()
    gui.moveTo(x=800, y=600)

    if "new tab" in text or "new tab kholo" in text or "naya tab" in text or "naya tab kholo" in text:
        open_new_tab()
    elif "close tab" in text or "tab band karo" in text or "tab close" in text or "close the tab" in text or "close this tab" in text:
        close_current_tab()
    elif "find" in text or "search" in text:
        open_browser_menu()
    elif "zoom in" in text or "bada karo" in text or "zoom karo" in text:
        zoom_in()
    elif "zoom out" in text or "chhota karo" in text or "zoom out karo" in text or "chhota karo" in text:
        zoom_out()
    elif "forward" in text or "aage jao" in text  or "aage bado" in text or "go forward" in text:
        go_forward()
    elif "back" in text or "peeche jao" in text or "go back" in text or "peeche bado" in text:
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
    elif "scroll up" in text or "upar jao" in text :
        scroll_up()
    elif "scroll up" in text or "upar jao firse" in text:
        scroll_up()
    elif "click here" in text or "click karo" in text   or "yahan click karo" in text or "yahan click" in text:
        click_at_cursor()

    elif "move right" in text or "daaye jao" in text or "right jao" in text or "move right side" in text or "right side jao" in text:
        move_cursor_right()
    elif "move left" in text or "baaye jao" in text or "left jao" in text or "move left side" in text or "left side jao" in text:
        move_cursor_left()
    elif "move right again" in text or "daaye jao firse" in text or "right jao firse" in text or "move right side again" in text or "right side jao firse" in text:
        move_cursor_right()
    elif "move left again" in text or "baaye jao firse" in text or "left jao firse" in text or "move left side again" in text or "left side jao firse" in text:
        move_cursor_left()
    elif "move up" in text or "upar jao" in text or "move up side" in text or "up side jao" in text:
        move_cursor_up()
    elif "move down" in text or "neeche jao" in text or "move down side" in text or "down side jao" in text:
        move_cursor_down()
    if "private window" in text or "naya private window" in text:
        open_private_window()
    else:
        pass


