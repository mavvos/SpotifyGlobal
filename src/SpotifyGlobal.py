"""
Add (customizable) global hotkeys to Spotify!
https://github.com/mavvos/SpotifyGlobal
"""

import configparser
import keyboard
import psutil
from pywinauto import Application, findwindows


def main():
    # Read config file
    config = configparser.ConfigParser()
    if not config.read("config.ini"):
        input("No config.ini file found.\nEnter to quit...")
        return 1

    # Get Spotify window
    sp = get_spotify_app()
    if not sp:
        input("Spotify not found, make sure it's open and try again.\nEnter to quit...")
        return 1

    # Get hotkeys
    hotkeys = config["Hotkeys"]
    spotify_commands = config["Spotify Commands"]

    # Set hotkeys
    for cmd in spotify_commands:
        keyboard.add_hotkey(
            hotkeys[cmd], lambda cmd=cmd: sp.send_keystrokes(spotify_commands[cmd])
        )
    print(f"SpotifyGlobal is up and running.\n    {hotkeys['Quit']} to quit.")
    keyboard.wait(hotkey=hotkeys["Quit"])


def get_spotify_app():
    for process in psutil.process_iter():
        if "spotify.exe" in process.name().lower():
            try:
                # We iterate to get rid of helper processes with the same name.
                # Only the main Spotify window returns find_window()
                spotify = findwindows.find_window(process=process.pid)
                app = Application(backend="win32").connect(handle=spotify)
                return app.top_window()
            except Exception as e:
                pass
    return None


if __name__ == "__main__":
    main()
