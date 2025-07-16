#!/usr/bin/python3
"""
This program is to write in a file with a JSON format
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves in a file data with a JSON format, if the file doesn't exists
    create it.
    Args:
      - my_obj
      - filename: str
    """

    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(json.dumps(my_obj))
