#!/usr/bin/python3
"""
This program helps to write in a file and if it doesn't exist, it creates the file.
"""


def write_file(filename="", text=""):
        """
        Write in a file, if doesn't exists it creates the file
        Args:
        - filename: string
        - text: string
        """

        with open(filename, mode="w", encoding="utf-8") as _file:
            _file.write(text)

            return (len(text))
