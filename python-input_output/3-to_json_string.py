#!/usr/bin/python3
"""
This program is to convert dictionaries to JSON
"""


import json


def to_json_string(my_obj):
    """
    To convert a dict to a JSON format
    Args:
     - my_obj: dict
    """

    return (json.dumps(my_obj))
