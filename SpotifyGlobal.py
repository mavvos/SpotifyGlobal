"""
SpotifyGlobal:
Records key presses with 'keyboard' and uses 'pywinauto'
to send equivalent hotkey command to Spotify application.
"""

import os
import sys
import time
from pathlib import Path
from pywinauto.application import Application
import keyboard


# If you want to change hotkeys, refer to options.txt
COMMANDS_HOTKEYS = {
    "VolUp": "shift+8",
    "VolDown": "shift+2",
    "PrevTrack": "shift+4",
    "NextTrack": "shift+6",
    "PlayPause": "shift+5",
    "Back5s": "shift+1",
    "Forward5s": "shift+3",
    "Like": "shift+7",
    "Quit": "shift+9",
}


def main():
    """
    For some reason trying to use pywinauto Application().connect() doesn't work;
    Spotify executable name simply disappears in thin air to never be found
    I couldn't figure out a way to retrieve it so we could use an already
    opened instance, so on this program's execution it also starts Spotify.
    ¯\_(ツ)_/¯
    """

    # Check if script is bundled as executable
    if getattr(sys, "frozen", False):
        base_dir = Path(sys.executable).parent
        print("SpotifyGlobal: RUNNING AS EXECUTABLE")
    else:
        base_dir = Path(__file__).parent
        print("SpotifyGlobal: RUNNING AS PYTHON SCRIPT")

    options_file = base_dir.joinpath("options.txt")
    file_reader = []
    first_run = True

    if options_file.exists():
        with open(options_file, "r", encoding="utf-8") as file:
            file_reader = file.readlines()
        user_path = search_file("path=", file_reader)
        if len(file_reader) != 10:  # Catch incomplete file
            os.remove(options_file)
            user_path = default_path()
        else:
            first_run = False
    else:
        user_path = default_path()

    try:
        # Try to open Spotify
        sp = Application().start(rf"{user_path}")
        sp = sp["Chrome_Widget_Win0"]  # Spotify window name
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
            for key in list(COMMANDS_HOTKEYS):
                default = f"{key}={COMMANDS_HOTKEYS[key]}\n"
                file.write(default)
                # Append to file_reader to avoid redundancy.
                file_reader.append(default)

    hk = {}  # Keys to use
    for key in list(COMMANDS_HOTKEYS):
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
    """Searches config in file_list, returns value found"""
    for lines in file_list:
        if config in lines:
            value = lines.replace(config, "")  # Remove config
            return value.rstrip("\n")  # Remove EOL
    return None


def default_path():
    """Returns Spotify default path"""
    user_directory = Path.home()  # C:\Users\~\
    user_path = user_directory.joinpath("AppData", "Roaming", "Spotify", "Spotify.exe")
    if not user_path.exists():
        user_path = input(
            "Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n\n"
        )
    return user_path


if __name__ == "__main__":
    main()
