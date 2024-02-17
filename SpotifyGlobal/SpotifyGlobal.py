"""
             SpotifyGlobal
Add (customizable) global hotkeys to Spotify!

More at https://github.com/mavvos/SpotifyGlobal
"""

import os
import warnings
import keyboard
import pywinauto
from defaults import sg_quit, DEFAULT_HK, DEFAULT_COMMANDS
from options_handler import OptionsHandler


def main():
    warnings.simplefilter("ignore", category=UserWarning)  # Ignore pywinauto warning
    default_options_file = "options.txt"
    default_options_len = 9
    options = OptionsHandler(default_options_file, default_options_len)
    options.set_directory()

    # Options file checking
    if options.file_exists():
        options.read_file()
        if options.incomplete_file():
            os.remove(options.dir)
            options.write_default_keys(DEFAULT_HK)
    else:
        options.write_default_keys(DEFAULT_HK)

    # Connect to Spotify
    try:
        app = pywinauto.Application().connect(title="Spotify")
    except pywinauto.findwindows.ElementNotFoundError:
        # If no perfect match, cast a bigger net and look for a generic name.
        # While this usually works, if Spotify is not open this might unintentionally
        # connect to the wrong window. This also seems to never raise exceptions.
        app = pywinauto.Application().connect(best_match="Chrome_Widget_Win0")
    finally:
        sp = app["Chrome_Widget_Win0"]

    # Catch connections to the wrong window
    if "Spotify" not in str(app.windows()):
        sg_quit("Spotify not found, make sure it's open and maximized then try again.")

    # Get Hotkeys
    hk = options.read_set_keys(DEFAULT_HK)
    if not hk:
        sg_quit("Couldn't set or find hotkeys.\nPlease try again.")

    # Setup Hotkeys
    for key, cmd in zip(hk, DEFAULT_COMMANDS):
        keyboard.add_hotkey(hk[key], lambda cmd=cmd: sp.send_keystrokes(cmd))
    print(f"SpotifyGlobal is up and running.\n    {hk['Quit']} to quit.")
    keyboard.wait(hotkey=hk["Quit"])


if __name__ == "__main__":
    main()
