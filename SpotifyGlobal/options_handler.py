""" SpotifyGlobal options handler """

import sys
from pathlib import Path


class OptionsHandler:
    """Handle SpotifyGlobal options file."""

    def __init__(self, file: str, lines: int) -> None:
        """
        Initialize options file handler

        * file = name of file to handle.
        * lines = default length of lines in that file.
        """
        self.file = file
        self.lines = lines
        self.dir = None
        self.file_content = None

    def running_as_exe(self) -> bool:
        """Check if application is being run as an executable, returns boolean"""
        if getattr(sys, "frozen", False):
            return True
        return False

    def file_exists(self) -> bool:
        """Check if file exists, returns boolean"""
        if self.dir.exists():
            return True
        return False

    def set_directory(self) -> None:
        """Set file directory based on parents directory"""
        if getattr(sys, "frozen", False):
            self.dir = (Path(sys.executable).parent).joinpath(self.file)
        else:
            self.dir = (Path(__file__).parent).joinpath(self.file)

    def incomplete_file(self) -> bool | None:
        """
        Check if file_content has the same length as defined by lines on class initialization,
        returns boolean.
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

    def read_file(self) -> None:
        """Open file and read it's content to self.file_content"""
        try:
            with open(self.dir, "r") as file:
                self.file_content = file.readlines()
        except FileNotFoundError:
            print(f"> read_file error: {self.file} does not exist.")

    def search_file(self, arg: str) -> str | None:
        """
        Searches for argument in file content,
        returns value found or None.
        """
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

    def write_default_keys(self, hk_dict: dict) -> None:
        """Create an options file in file's directory with given argument dictionary."""
        with open(self.dir, "a") as file:
            for key in hk_dict:
                default = f"{key}={hk_dict[key]}\n"
                file.write(default)
        self.read_file()  # In case file does not exist, read file to get new default hotkeys

    def read_set_keys(self, hk_dict: dict) -> dict:
        """
        Loop over each key in argument dictionary, call search_file() for each key.
        If value returned is valid, append to a new dictionary.

        Returns new dictionary.
        """
        hk = {}
        for key in hk_dict:
            config = f"{key}"
            value = self.search_file(config)
            if value is not None:
                hk[config] = value
        return hk
