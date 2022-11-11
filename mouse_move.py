import pyautogui
import time
import webbrowser
import pyperclip

webbrowser.open("https://google.com")
time.sleep(1)
pyperclip.copy("平泉町 観光")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("mouse_move_2.png")
