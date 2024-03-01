#!/usr/bin/python3
""" Base class """
import json
import csv
from collections import OrderedDict
import turtle


class Base:
    """ defin the base class for all the other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Assign the public instance attribute id

        Args:
            id(int): integer valuefor ids

        Return:
            Always nothing.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

