""" SpotifyGlobal options handler """

import sys
from pathlib import Path


class OptionsHandler:
    """Handle SpotifyGlobal options file."""

    def __init__(self, file: str, lines: int) -> None:
        """file = File name.\n
        lines = Default length of file.
        """
        self.file = file
        self.lines = lines
        self.dir = ""
        self.file_content = ""
        self.spotify_path = ""

    def set_directory(self) -> None:
        """Set file directory based on parents directory."""
        if getattr(sys, "frozen", False):
            self.dir = (Path(sys.executable).parent).joinpath(self.file)
        else:
            self.dir = (Path(__file__).parent).joinpath(self.file)

    def file_exists(self) -> bool:
        """Check if file exists, returns boolean."""
        if self.dir.exists():
            return True
        return False

    def read_file(self) -> None:
        """Read file content to file_content."""
        try:
            with open(self.dir, "r") as file:
                self.file_content = file.readlines()
        except FileNotFoundError:
            print(f"> read_file error: {self.file} does not exist.")

    def incomplete_file(self) -> bool | None:
        """Check if file_content has same length as defined lines on class call.

        Returns True or False.
        """
        try:
            if len(self.file_content) != self.lines:
                return True
            return False
        except AttributeError:
            print(
                f"> catch_incomplete error: {self.file}\
                has not been read, read_file() must be executed first."
            )
            return None

    def search_file(self, arg) -> str | None:
        """Searches for argument in file content,
        returns value found or None."""
        try:
            for lines in self.file_content:
                if arg in lines:
                    value = lines.replace(f"{arg}=", "")  # Remove argument
                    return value.rstrip("\n")  # Remove EOL
            return None
        except AttributeError:
            print(
                f"> look_in_file error: {self.file}\
                has not been read, read_file() must be executed first."
            )
            return None

    def spotify_default_path(self) -> None:
        """Check if Spotify exists in default directory,
        if yes set spotify_path to it.
        """
        user_directory = Path.home()
        default_path = user_directory.joinpath(
            "AppData", "Roaming", "Spotify", "Spotify.exe"
        )
        if default_path.exists():
            self.spotify_path = default_path

    def running_as_exe(self) -> bool:
        """Returns True if script is being run as an executable"""
        if getattr(sys, "frozen", False):
            return True
        return False

    def write_default_keys(self, hk_dict: dict) -> None:
        """Creates options file based on default configurations (by argument dictionary).

        'Path=' is set as current spotify_path.
        """
        try:
            with open(self.dir, "a") as file:
                file.write(f"path={self.spotify_path}\n")
                for key in hk_dict:
                    default = f"{key}={hk_dict[key]}\n"
                    file.write(default)
            self.read_file()  # In case file does not exist, read file to get new default hotkeys
        except AttributeError:
            # In case Spotify default_path does not exist, input user for path
            self.spotify_path = self.input_path()

    def read_set_keys(self, hk_dict: dict) -> dict:
        """Read set configurations values from file_content based in given dictionary keys.

        Calls search_file for each dict key then append key value to new dictionary.
        Only includes keys with found values in the result dictionary.

        Returns new dictionary.
        """
        hk = {}
        for key in hk_dict:
            config = f"{key}"
            value = self.search_file(config)
            if value is not None:
                hk[config] = value
        return hk

    def input_path(self) -> str:
        """Manually input user for Spotify path, returns string input"""
        print("Spotify not found.")
        return input(
            "Type your Spotify path\n\
Paths should look something like:\n\
C:\\Users\\YOU\\AppData\\Roaming\\Spotify\\Spotify.exe\n\n"
        )
