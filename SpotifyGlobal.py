"""
             SpotifyGlobal
Add (customizable) global hotkeys to Spotify!

More at https://github.com/mavvos/SpotifyGlobal
"""

import os
import keyboard
from pywinauto.application import Application, AppStartError
from SGHelper import sg_quit, DEFAULT_HK, DEFAULT_COMMANDS
from SGOptions import OptionsUtils


def main():
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
                # In case file exists, it's complete but PATH still missing
                print("PATH NOT FOUND")
            os.remove(options.dir)
            options.spotify_default_path()
            options.write_default_keys(DEFAULT_HK)
    else:
        options.spotify_default_path()
        options.write_default_keys(DEFAULT_HK)

    # Open Spotify
    try:
        # We can't use pywinauto Application.connect
        # because Spotify executable name changes with every song.
        sp = Application().start(rf"{options.spotify_path}")
        sp = sp["Chrome_Widget_Win0"]  # Default Spotify window name
    except AppStartError:
        sg_quit(
            "Couldn't open Spotify. PATH typed is wrong or options.txt has the wrong PATH.\n\nTry again"
        )

    # Get Hotkeys
    hk = options.read_set_keys(DEFAULT_HK)
    if not hk:
        sg_quit("Couldn't set or find hotkeys.\nPlease try again.")

    # Setup Hotkeys
    for key, cmd in zip(hk, DEFAULT_COMMANDS):
        keyboard.add_hotkey(hk[key], lambda cmd=cmd: sp.send_keystrokes(cmd))
    print(f"SpotifyGlobal is up and running.    {hk['Quit']} to quit.")
    keyboard.wait(hotkey=hk["Quit"])


if __name__ == "__main__":
    main()
