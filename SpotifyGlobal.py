"""
Spotify controlled by Global Hotkeys.
Registers key presses with 'keyboard' and uses 'pywinauto'
to send equivalent hotkey command to Spotify application.
"""

import sys
import time
from pathlib import Path
from pywinauto.application import Application
import keyboard


# If you want to change hotkeys, please refer to options.txt
HOTKEY_COMMANDS = [
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

DEFAULT_HOTKEYS = [
    "shift+8",
    "shift+2",
    "shift+4",
    "shift+6",
    "shift+5",
    "shift+1",
    "shift+3",
    "shift+7",
    "shift+9",
]

HOTKEY_AMOUNT = len(HOTKEY_COMMANDS)


def main():
    """
    For some reason trying to use pywinauto's Application().connect() doesn't work;
    Spotify's executable name simply disappears in thin air to never be found
    and I couldn't figure out a way to retrieve it so I could use an already
    opened instance, so on this program's execution it also starts Spotify.
    ¯\_(ツ)_/¯
    """

    if getattr(sys, "frozen", False):  # Check if script is bundled as executable
        base_dir = Path(sys.executable).parent
        print("SpotifyGlobal: RUNNING AS EXECUTABLE")
    else:
        base_dir = Path(__file__).parent
        print("SpotifyGlobal: RUNNING AS PYTHON SCRIPT")

    options_file = base_dir.joinpath("options.txt")
    file_reader = []

    if options_file.exists():
        with open(options_file, "r", encoding="utf-8") as file:
            file_reader = file.readlines()
        options_exists = True
    else:
        options_exists = False

    if options_exists:
        config = "path="  # Search path in options
        for lines in file_reader:
            if config in lines:
                value = lines[len(config) : -1]
                break
        user_path = value
        user_inputted_path = False
    else:
        # Try Spotify default path
        user_directory = Path.home()  # C:\Users\~\
        user_path = user_directory.joinpath(
            "AppData", "Roaming", "Spotify", "Spotify.exe"
        )
        if user_path.exists():
            print("Spotify found on default installation path.\n")
            user_inputted_path = True
        else:
            # If both fail, input user for path
            user_path = input(
                "Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n\n"
            )
            user_inputted_path = True

    try:
        # Try to open Spotify
        sp = Application().start(rf"{user_path}")
        sp = sp["Chrome_Widget_Win0"]
    except:
        print(
            "Couldn't open Spotify.\n\
Either PATH typed is wrong or\n\
options.txt has the wrong PATH.\n\n\
Try again"
        )
        time.sleep(4)
        sys.exit(1)

    if user_inputted_path:  # Save path in options.txt
        with open(options_file, "a", encoding="utf-8") as file:
            file.write(f"path={user_path}\n")

    if not options_exists:  # Add default hotkeys to options.txt
        with open(options_file, "a", encoding="utf-8") as file:
            for i in range(HOTKEY_AMOUNT):
                file.write(f"{HOTKEY_COMMANDS[i]}={DEFAULT_HOTKEYS[i]}\n")

                # Append to file_reader to avoid rereading
                file_reader.append(f"{HOTKEY_COMMANDS[i]}={DEFAULT_HOTKEYS[i]}\n")

    # Read options.txt for hotkeys and append key:value to hk{}
    hk = {}
    for i in range(HOTKEY_AMOUNT):
        config = f"{HOTKEY_COMMANDS[i]}="
        for lines in file_reader:
            if config in lines:
                value = lines[len(config) : -1]
                hk.update({config: value})
                break

    keyboard.add_hotkey(hk["VolUp="], lambda: sp.send_keystrokes("^{UP}"))
    keyboard.add_hotkey(hk["VolDown="], lambda: sp.send_keystrokes("^{DOWN}"))
    keyboard.add_hotkey(hk["PrevTrack="], lambda: sp.send_keystrokes("^{LEFT}"))
    keyboard.add_hotkey(hk["NextTrack="], lambda: sp.send_keystrokes("^{RIGHT}"))
    keyboard.add_hotkey(hk["PlayPause="], lambda: sp.send_keystrokes("{SPACE}"))
    keyboard.add_hotkey(hk["Back5s="], lambda: sp.send_keystrokes("+{LEFT}"))
    keyboard.add_hotkey(hk["Forward5s="], lambda: sp.send_keystrokes("+{RIGHT}"))
    keyboard.add_hotkey(hk["Like="], lambda: sp.send_keystrokes("%+{B}"))

    print(
        f"\nApplication is up and running, keep this window open.\n\n\
To quit application press {hk['Quit=']} or close this window.\n\
        Spotify will stay open."
    )

    keyboard.wait(hotkey=hk["Quit="])  # Keep running until key


if __name__ == "__main__":
    main()
