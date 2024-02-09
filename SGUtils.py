""" SpotifyGlobal Utilities """

import sys
from pathlib import Path


class OptionsUtils:

    def __init__(self, file: str, len: int) -> None:
        """File name, Default length of file."""
        self.file = file
        self.len = len

    def set_directory(self) -> None:
        """Set directory based on parent directory"""
        if getattr(sys, "frozen", False):
            self.dir = (Path(sys.executable).parent).joinpath(self.file)
        else:
            self.dir = (Path(__file__).parent).joinpath(self.file)

    def file_exists(self) -> bool:
        if self.dir.exists():
            return True
        return False

    def read_file(self) -> None:
        try:
            with open(self.dir, "r") as file:
                self.file_content = file.readlines()
        except FileNotFoundError:
            print(f"> read_file error: {self.file} does not exist.")

    def incomplete_file(self) -> bool | None:
        try:
            if len(self.file_content) != self.len:
                return True
            return False
        except AttributeError:
            print(
                f"> catch_incomplete error: {self.file} has not been read, read_file() must be executed first."
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
                f"> look_in_file error: {self.file} has not been read, read_file() must be executed first."
            )
            return None

    def spotify_default_path(self) -> None:
        default_path = Path.home().joinpath(
            "AppData", "Roaming", "Spotify", "Spotify.exe"
        )
        if default_path.exists():
            self.spotify_path = default_path

    def running_as_exe(self) -> bool:
        """Returns True if file is running as executable."""
        if getattr(sys, "frozen", False):
            return True
        return False

    def write_default_keys(self, hk_dict: dict) -> None:
        with open(self.dir, "a") as file:
            file.write(f"path={self.spotify_path}\n")
            for key in hk_dict:
                default = f"{key}={hk_dict[key]}\n"
                file.write(default)
        self.read_file()

    def read_set_keys(self, hk_dict: dict) -> dict:
        hk = {}
        for key in hk_dict:
            config = f"{key}"
            value = self.search_file(config)
            if value is not None:
                hk[config] = value
        return hk
