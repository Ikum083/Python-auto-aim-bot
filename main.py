# importing packages
from pyautogui import *
import pyautogui
import time
import keyboard
from win32 import win32api
import win32con
import customtkinter as ctk
import threading

# creating window
window = ctk.CTk()
window.geometry("400x150")
window.title("Python Auto Aim")
window.grid_columnconfigure(0, weight = 1)
window.grid_rowconfigure(0, weight = 1)

# function to automate mouse click and hover
def clicked(x ,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENETF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTUP,0,0)

# function to replace running label to inform user if the program is running
def update_running_label(text):
    print("ran")
    running_label.configure(text = text)

# function to run the auto aim bot 
## r = 255, g = 219, b = 195 : Color of the target
def auto_aim_on():
    update_running_label("Program is currently running")
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
    else:
        update_running_label("Program is currently not running")

# main function
def main():
    thread = threading.Thread(target = auto_aim_on)
    thread.daemon = True
    thread.start()
    
# button to activate the auto aim
auto_aim_button = ctk.CTkButton(window, text = "Turn on auto aim", command=main)
auto_aim_button.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "ew")

# label to tell user to press 'q' to deactivate the auto aim bot
user_label = ctk.CTkLabel(window, text = "Press 'q' to deactivate the auto aim bot")
user_label.grid(row = 1, column = 0)

# label to tell user that program is current running or not
running_label = ctk.CTkLabel(window, text = "Program is currently not running")
running_label.grid(row = 2, column = 0)

# main loop to continuously run the window
window.mainloop()