# Spotify controlled by Global Hotkeys.
# This program registers key presses and uses pywinauto
# to send equivalent hotkey command to Spotify application.

# Hotkey in Program = Expected Command
# SHIFT + 8         = Volume Up      
# SHIFT + 2         = Volume Down    
# SHIFT + 4         = Previous Track 
# SHIFT + 6         = Next Track     
# SHIFT + 5         = Play/Pause     
# SHIFT + 1         = Go back 5 seconds   
# SHIFT + 3         = Go forward 5 seconds   
# SHIFT + 7         = Like/Dislike Track
# SHIFT + 9         = QUIT PROGRAM

from pywinauto.application import Application
import csv
import os
import keyboard
import time

    
def main():
    # For some reason trying to use pywinauto.Application().connect() doesn't work;
    # Spotify's executable name simply disappears in thin air to never be found
    # and I couldn't figure out a way to retrieve it so I could use an already
    # opened instance, so on this program's execution it also starts Spotify.
    # ¯\_(ツ)_/¯

    try:
        # Try to find user path in preferences
        bundle_dir = os.path.abspath(os.path.dirname(__file__))
        preferences = os.path.join(bundle_dir, "preferences.csv")
        with open(f"{preferences}", "r") as file:
            buffer = csv.reader(file)
            for row in buffer:
                user_path = "".join(row)
    except:
        # If no preferences, input user for path
        user_path = str("path=") + input("Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n")
        user_path = "".join(user_path)
        print()
        # And then create user default path with input
        with open(f"{preferences}", "w") as file:
            file.write(user_path)

    try:
        # Try to open Spotify
        sp = Application().start(rf"{user_path[5:]}")
        sp = sp["Chrome_Widget_Win0"]
        print()
    except:
        # Error message
        print("\nCouldn't open Spotify.\n\
Either PATH typed is wrong or\n\
preferences.csv file has the wrong PATH.\n\n\
Try again")
        # Delete preferences file if invalid path
        if os.path.exists(preferences) and os.path.isfile(preferences):
            os.remove(preferences)
        time.sleep(4)
        exit(1)

    # Set up hotkeys
    keyboard.add_hotkey('shift+8', lambda: sp.send_keystrokes('^{UP}'), time.sleep(1))
    keyboard.add_hotkey('shift+2', lambda: sp.send_keystrokes('^{DOWN}'), time.sleep(1))
    keyboard.add_hotkey('shift+4', lambda: sp.send_keystrokes('^{LEFT}'), time.sleep(1))
    keyboard.add_hotkey('shift+6', lambda: sp.send_keystrokes('^{RIGHT}'), time.sleep(1))
    keyboard.add_hotkey('shift+5', lambda: sp.send_keystrokes('{SPACE}'), time.sleep(1))
    keyboard.add_hotkey('shift+1', lambda: sp.send_keystrokes('+{LEFT}'), time.sleep(1))
    keyboard.add_hotkey('shift+3', lambda: sp.send_keystrokes('+{RIGHT}'), time.sleep(1))
    keyboard.add_hotkey('shift+7', lambda: sp.send_keystrokes('%+{B}'), time.sleep(1))

    # Running message
    print("Aplication is up and running, keep this window open.\n\n\
To quit application press SHIFT + 9 or close this window.\n\
        Spotify will stay open.")

    # Keep program running on background until quit hotkey
    keyboard.wait(hotkey="shift+9") # Quit on hotkey


main()
