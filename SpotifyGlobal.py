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
from SGUtils import OptionsUtils
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

    default_options_file = "options.txt"
    default_options_len = 10

    options = OptionsUtils(default_options_file, default_options_len)

    options.set_directory()

    # Options file checking
    if options.file_exists():
        options.read_file()
        user_path = options.search_file("path")

        if user_path:
            options.spotify_path = user_path
        else:
            if not options.incomplete_file():
                print("PATH NOT FOUND")
            os.remove(options.dir)
            options.spotify_default_path()
            options.write_default_keys(COMMANDS_HOTKEYS)

    else:
        options.spotify_default_path()
        options.write_default_keys(COMMANDS_HOTKEYS)

    # Try to Open Spotify here
    #
    #    PLACEHOLDER
    #

    # Read hotkeys
    hk = options.read_set_keys(COMMANDS_HOTKEYS)

    # HOTKEYS FUNCTIONALITY
    #
    #    PLACEHOLDER
    #

    keyboard.add_hotkey(hk["VolUp"], lambda: sp.send_keystrokes("^{UP}"))
    keyboard.add_hotkey(hk["VolDown"], lambda: sp.send_keystrokes("^{DOWN}"))
    keyboard.add_hotkey(hk["PrevTrack"], lambda: sp.send_keystrokes("^{LEFT}"))
    keyboard.add_hotkey(hk["NextTrack"], lambda: sp.send_keystrokes("^{RIGHT}"))
    keyboard.add_hotkey(hk["PlayPause"], lambda: sp.send_keystrokes("{SPACE}"))
    keyboard.add_hotkey(hk["Back5s"], lambda: sp.send_keystrokes("+{LEFT}"))
    keyboard.add_hotkey(hk["Forward5s"], lambda: sp.send_keystrokes("+{RIGHT}"))
    keyboard.add_hotkey(hk["Like"], lambda: sp.send_keystrokes("%+{B}"))

    print(
        f"\nApplication is up and running, keep this window open.\n\n\
To quit application press {hk['Quit']} or close this window.\n\
        Spotify will stay open."
    )

    keyboard.wait(hotkey=hk["Quit"])  # Keep running until key


if __name__ == "__main__":
    main()
