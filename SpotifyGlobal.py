# Spotify controlled by Global Hotkeys.
# Registers key presses with 'keyboard' and uses 'pywinauto'
# to send equivalent hotkey command to Spotify application.

import sys
import time
from pywinauto.application import Application
import keyboard
from pathlib import Path


# If you want to change hotkeys, please refer to options.txt
# Default hotkeys
default_hotkeys = [
    "VolUp=shift+8",
    "VolDown=shift+2",
    "PrevTrack=shift+4",
    "NextTrack=shift+6",
    "PlayPause=shift+5",
    "Back5s=shift+1",
    "Forward5s=shift+3",
    "Like=shift+7",
    "Quit=shift+9",
]


def main():
    # For some reason trying to use pywinauto's Application().connect() doesn't work;
    # Spotify's executable name simply disappears in thin air to never be found
    # and I couldn't figure out a way to retrieve it so I could use an already
    # opened instance, so on this program's execution it also starts Spotify.
    # ¯\_(ツ)_/¯

    # Determine the correct path to write the file depending on how it's running
    if getattr(sys, "frozen", False):  # Check if script is bundled as executable
        base_dir = Path(sys.executable).parent

        print("SpotifyGlobal: RUNNING AS EXECUTABLE")
    else:
        base_dir = Path(__file__).parent
        print("SpotifyGlobal: RUNNING AS PYTHON SCRIPT")

    options_file = base_dir.joinpath("options.txt")

    # Check if options.txt exists
    if options_file.exists:
        # If yes, open options.txt and read contents to a list
        with open(options_file, "r") as file:
            file_reader = file.readlines()
        options_exists = True
    else:
        options_exists = False

    if options_exists:
        # Read options for path
        print('Found options.txt, looking for "path="\n')
        config = "path="
        for lines in file_reader:
            if config in lines:
                value = lines[len(config) : -1]
                break
        user_path = value
        user_inputed_path = False
    else:
        # If no options, try Spotify default path
        user_directory = Path.home()  # C:\Users\~\
        user_path = user_directory.joinpath(
            "AppData", "Roaming", "Spotify", "Spotify.exe"
        )
        if user_path.exists:
            # File found
            print("Spotify found on default installation path.\n")
            user_inputed_path = (
                True  # Pretend user inputed to save default path in options.txt
            )
        else:
            # If no options and Spotify not found, input user for path
            user_path = input(
                "Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n"
            )
            print()
            user_inputed_path = True

    try:
        # Try to open Spotify
        sp = Application().start(rf"{user_path}")
        sp = sp["Chrome_Widget_Win0"]
    except:
        # Error message
        print(
            "Couldn't open Spotify.\n\
Either PATH typed is wrong or\n\
options.txt has the wrong PATH.\n\n\
Try again"
        )
        time.sleep(4)
        sys.exit(1)

    # If user inputed path, save it in options.txt
    if user_inputed_path is True:
        with open(options_file, "a") as file:
            file.write(f"path={user_path}\n")

    # If user first time opening, add default hotkeys to options.txt
    if options_exists is False:
        with open(options_file, "a") as file:
            for i in range(len(default_hotkeys)):
                file.write(f"{default_hotkeys[i]}\n")

    # If user first time, read options.txt again to get recently added hotkeys
    if options_exists is False:
        with open(options_file, "r") as file:
            file_reader = file.readlines()

    hk = {}  # Dict of Hotkeys to use
    # Read options.txt for hotkeys and append key:value to hk{}
    hotkey_commands = [
        "VolUp",
        "VolDown",
        "PrevTrack",
        "NextTrack",
        "PlayPause",
        "Back5s",
        "Forward5s",
        "Like",
        "Quit",
    ]
    for i in range(len(hotkey_commands)):
        config = f"{hotkey_commands[i]}="
        for lines in file_reader:
            if config in lines:
                value = lines[len(config) : -1]
                hk.update({config: value})
                break

    # Set up hotkeys
    keyboard.add_hotkey(
        hk["VolUp="], lambda: sp.send_keystrokes("^{UP}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        hk["VolDown="], lambda: sp.send_keystrokes("^{DOWN}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        hk["PrevTrack="], lambda: sp.send_keystrokes("^{LEFT}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        hk["NextTrack="], lambda: sp.send_keystrokes("^{RIGHT}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        hk["PlayPause="], lambda: sp.send_keystrokes("{SPACE}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        hk["Back5s="], lambda: sp.send_keystrokes("+{LEFT}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        hk["Forward5s="], lambda: sp.send_keystrokes("+{RIGHT}"), time.sleep(1)
    )
    keyboard.add_hotkey(hk["Like="], lambda: sp.send_keystrokes("%+{B}"), time.sleep(1))

    # Program running message
    print(
        f"\nApplication is up and running, keep this window open.\n\n\
To quit application press {hk['Quit=']} or close this window.\n\
        Spotify will stay open."
    )

    # Keep program running on background until quit hotkey
    keyboard.wait(hotkey=hk["Quit="])  # Quit on hotkey


main()
