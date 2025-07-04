#!/usr/bin/python3
"""This defines the function of class_checking."""


def is_same_class(obj, a_class):
    """To tell if an object is exactly an instance of the given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
