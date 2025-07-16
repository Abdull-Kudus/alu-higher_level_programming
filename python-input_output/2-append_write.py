#!/usr/bin/python3
"""
This program helps to  append text in a file,
create the file if it doesn't exists
"""


def append_write(filename="", text=""):
    """
    Append the text to the end of the file, and create if doesn't exists.
    Args:
      - filename: string
      - text: string
    """

    with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
