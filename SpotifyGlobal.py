"""
Spotify controlled by Global Hotkeys.
Registers key presses with 'keyboard' and uses 'pywinauto'
to send equivalent hotkey command to Spotify application.
"""
import json
import sys
import time
from pathlib import Path
from pywinauto.application import Application
import keyboard


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
    '''
    For some reason trying to use pywinauto's Application().connect() doesn't work;
    Spotify's executable name simply disappears in thin air to never be found
    and I couldn't figure out a way to retrieve it so I could use an already
    opened instance, so on this program's execution it also starts Spotify.
   '''
    if getattr(sys, "frozen", False):  # Check if script is bundled as executable
        base_dir = Path(sys.executable).parent
        print("SpotifyGlobal: RUNNING AS EXECUTABLE")
    else:
        base_dir = Path(__file__).parent
        print("SpotifyGlobal: RUNNING AS PYTHON SCRIPT")

    options_file = base_dir.joinpath("options.json")

    if options_file.exists():
        with open(options_file) as file:
            diz: dict = json.load(file)
        user_path = Path(diz["Path"])
    else:
        diz = dict(zip(HOTKEY_COMMANDS, DEFAULT_HOTKEYS))
        user_directory = Path.home()  
        user_path = user_directory.joinpath(
            "AppData", "Roaming", "Spotify", "Spotify.exe"
        )
        if user_path.exists():
            diz["Path"] = str(user_path)
        else:
            while not user_path.exists():
                user_path = Path(
                    input(
                        "Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n"
                    )
                )
        with open(options_file, "w") as file:
            diz["Path"] = str(user_path)
            json.dump(diz, file)

    try:
        # Try to open Spotify
        sp = Application().start(str(user_path))
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

    keyboard.add_hotkey(
        diz["VolUp"], lambda: sp.send_keystrokes("^{UP}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        diz["VolDown"], lambda: sp.send_keystrokes("^{DOWN}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        diz["PrevTrack"], lambda: sp.send_keystrokes("^{LEFT}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        diz["NextTrack"], lambda: sp.send_keystrokes("^{RIGHT}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        diz["PlayPause"], lambda: sp.send_keystrokes("{SPACE}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        diz["Back5s"], lambda: sp.send_keystrokes("+{LEFT}"), time.sleep(1)
    )
    keyboard.add_hotkey(
        diz["Forward5s"], lambda: sp.send_keystrokes("+{RIGHT}"), time.sleep(1)
    )
    keyboard.add_hotkey(diz["Like"], lambda: sp.send_keystrokes("%+{B}"), time.sleep(1))

    print(
        f"\nApplication is up and running, keep this window open.\n\n\
To quit application press {diz['Quit']} or close this window.\n\
        Spotify will stay open."
    )
    keyboard.wait(hotkey=diz["Quit"])


main()
