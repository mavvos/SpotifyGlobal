"""
             SpotifyGlobal
Add (customizable) global hotkeys to Spotify!

Source at https://github.com/mavvos/SpotifyGlobal
"""

import configparser
import keyboard
import pywinauto


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Connect to Spotify
    try:
        app = pywinauto.Application().connect(title="Spotify")
    except pywinauto.findwindows.ElementNotFoundError:
        # If we can't find Spotify's exact window, look for a generic name.
        # While this usually works, it can unintentionally connect to the wrong window.
        # Because it always connects to a window, it also never raises exceptions.
        app = pywinauto.Application().connect(best_match="Chrome_Widget_Win0")
    finally:
        sp = app["Chrome_Widget_Win0"]

    # Catch connections to the wrong window
    if "spotify" not in str(app.windows()).lower():
        input("Connected to the wrong window. Press Enter to quit...")
        return 1

    # Get Hotkeys
    hotkeys = config["Hotkeys"]
    spotify_commands = config["Spotify Commands"]

    # Set Hotkeys
    for cmd in spotify_commands:
        keyboard.add_hotkey(
            hotkeys[cmd], lambda cmd=cmd: sp.send_keystrokes(spotify_commands[cmd])
        )
    print(f"SpotifyGlobal is up and running.\n    {hotkeys['Quit']} to quit.")
    keyboard.wait(hotkey=hotkeys["Quit"])


if __name__ == "__main__":
    main()
