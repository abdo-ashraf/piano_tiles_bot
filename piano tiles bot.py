import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(300,300)[0] == 0:
        click(300,300)
    if pyautogui.pixel(375,300)[0] == 0:
        click(375,300)
    if pyautogui.pixel(450,300)[0] == 0:
        click(450,300)
    if pyautogui.pixel(525,300)[0] == 0:
        click(525,300)

## https://www.agame.com/game/magic-piano-tiles
