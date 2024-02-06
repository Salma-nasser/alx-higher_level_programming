#!/usr/bin/python3
""" A class of square with optional size and type/value validation"""


class Square:
    """define a class of square"""
    def __init__(self, size=0):
        """initialize the square class with a size that is positive"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Calculating the area of the square using the given size"""
        return (self.__size ** 2)
