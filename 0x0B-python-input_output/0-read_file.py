#!/usr/bin/python3
"""
reading a file
"""


def read_file(filename=""):
    """  the function defination """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
