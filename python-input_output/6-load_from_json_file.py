#!/usr/bin/python3
"""
This program is to read files .json and to convert into types of python
"""


import json


def load_from_json_file(filename):
    """
    To read a file and to convert the content (JSON) to python types
    Args:
      - filename: path
    """

    with open(filename, mode="r", encoding="utf-8") as _file:
        return (json.loads(_file.read()))
