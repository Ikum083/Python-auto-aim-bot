# importing packages
from pyautogui import *
import pyautogui
import time
import keyboard
import random
from win32 import win32api
import win32con
import cv2

# function to automate mouse click and hover
def clicked(x ,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEVENETF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTUP,0,0)

# function to run the auto aim bot 
## r = 255, g = 219, b = 195 : Color of the target
def auto_aim_on():
    screenshot_x_coordinate = 1020
    screenshot_y_coordinate = 400
    screenshot_size_x = 800
    screenshot_size_y = 600
    while keyboard.is_pressed('q') == False:
        img = pyautogui.screenshot(region=(screenshot_x_coordinate, screenshot_y_coordinate, screenshot_size_x, screenshot_size_y))
        width, height = img.size
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = img.getpixel((x,y))
                if r == 255 and g == 219 and b == 195:
                    click(x + screenshot_x_coordinate, y + screenshot_y_coordinate)
                    time.sleep(0.05)
                    break

auto_aim_on()