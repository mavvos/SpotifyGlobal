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
        user_path = search_file("path=", file_reader)
        first_run = False
    else:
        # Try Spotify default path
        first_run = True
        user_directory = Path.home()  # C:\Users\~\
        user_path = user_directory.joinpath(
            "AppData", "Roaming", "Spotify", "Spotify.exe"
        )
        if user_path.exists():
            print("Spotify found on default installation path.\n")
        else:
            # If all fails, input user for path
            user_path = input(
                "Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n\n"
            )

    try:
        # Try to open Spotify
        sp = Application().start(rf"{user_path}")
        sp = sp["Chrome_Widget_Win0"]  # Spotify's window name
    except:
        print(
            "Couldn't open Spotify.\n\
Either PATH typed is wrong or\n\
options.txt has the wrong PATH.\n\n\
Try again"
        )
        time.sleep(4)
        sys.exit(1)

    if first_run:  # Save user path and default hotkeys in options.txt
        with open(options_file, "a", encoding="utf-8") as file:
            file.write(f"path={user_path}\n")
            for key, default in zip(HOTKEY_COMMANDS, DEFAULT_HOTKEYS):
                file.write(f"{key}={default}\n")
                # Append to file_reader to avoid redundancy.
                file_reader.append(f"{key}={default}\n")

    hk = {}  # Keys to use
    for key in HOTKEY_COMMANDS:
        config = f"{key}="
        value = search_file(config, file_reader)
        if value is not None:
            hk[config] = value

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


def search_file(config, file_list):
    """Config is what you're looking for,
    file_list is list to search on.
    Returns value found on file.
    """
    for lines in file_list:
        if config in lines:
            value = lines.replace(config, "")  # Remove config
            return value.rstrip("\n")  # Remove EOL
    return None


if __name__ == "__main__":
    main()
