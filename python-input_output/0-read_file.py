#!/usr/bin/python3
"""
This program is used to read files
"""


def read_file(filename=""):
    """
    This function reads a file and print out it contents
    """

    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
