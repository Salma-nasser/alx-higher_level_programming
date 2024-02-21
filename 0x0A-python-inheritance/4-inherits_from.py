#!/usr/bin/python3
"""Defines an inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """ return true if obj is from class """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    return (False)
