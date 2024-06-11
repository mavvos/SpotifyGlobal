""" SpotifyGlobal defaults """

import time
import sys

# If you want to change hotkeys, refer to options.txt
DEFAULT_HK = {
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


DEFAULT_COMMANDS = [
    "^{UP}",
    "^{DOWN}",
    "^{LEFT}",
    "^{RIGHT}",
    "{SPACE}",
    "+{LEFT}",
    "+{RIGHT}",
    "%+{B}",
]


def sg_quit(message: str) -> None:
    """Print argument message, sleep for set amount of time then quit by sys.exit(1)."""
    print(message)
    time.sleep(4)
    sys.exit(1)
