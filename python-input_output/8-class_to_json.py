#!/usr/bin/python3
"""
This program is to return the dict representation of an instance of a Class.
"""


def class_to_json(obj):
    """
    This returns the dictionary description with simple data structure
    Args:
      - obj: instance of class
    """

    return (obj.__dict__)
