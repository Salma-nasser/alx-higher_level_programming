#!/usr/bin/python3
""" defines an inherited list class Mylist.
"""


class MyList(list):
    """ Implements sorted printing for the built in list
    """

    def print_sorted(self):
        """prints a list in sorted asc order
        """
        print(sorted(self))
