"""
SpotifyGlobal: https://github.com/mavvos/SpotifyGlobal
"""

import os
from pywinauto.application import Application, AppStartError
from SGHelper import sg_quit, DEFAULT_HK
from SGOptions import OptionsUtils
import keyboard


def main():
    """
    For some reason trying to use pywinauto Application().connect() doesn't work;
    Spotify executable name simply disappears in thin air to never be found.
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
        sp = Application().start(rf"{options.spotify_path}")
        sp = sp["Chrome_Widget_Win0"]  # Spotify window name
    except AppStartError:
        sg_quit(
            "Couldn't open Spotify.\nEither PATH typed is wrong or options.txt has the wrong PATH.\n\nTry again"
        )

    # Hotkeys
    hk = options.read_set_keys(DEFAULT_HK)
    if not hk:
        sg_quit("Couldn't set or find hotkeys.\nPlease try again.")

    keyboard.add_hotkey(hk["VolUp"], lambda: sp.send_keystrokes("^{UP}"))
    keyboard.add_hotkey(hk["VolDown"], lambda: sp.send_keystrokes("^{DOWN}"))
    keyboard.add_hotkey(hk["PrevTrack"], lambda: sp.send_keystrokes("^{LEFT}"))
    keyboard.add_hotkey(hk["NextTrack"], lambda: sp.send_keystrokes("^{RIGHT}"))
    keyboard.add_hotkey(hk["PlayPause"], lambda: sp.send_keystrokes("{SPACE}"))
    keyboard.add_hotkey(hk["Back5s"], lambda: sp.send_keystrokes("+{LEFT}"))
    keyboard.add_hotkey(hk["Forward5s"], lambda: sp.send_keystrokes("+{RIGHT}"))
    keyboard.add_hotkey(hk["Like"], lambda: sp.send_keystrokes("%+{B}"))

    print(f"SpotifyGlobal is up and running.\n{hk['Quit']} to quit.")
    keyboard.wait(hotkey=hk["Quit"])


if __name__ == "__main__":
    main()
