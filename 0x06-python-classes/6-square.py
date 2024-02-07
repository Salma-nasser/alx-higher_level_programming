#!/usr/bin/python3
"""Class named Square with a specific size"""


class Square:
    """ A class that defines a square with specific size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square class with a size that has a positive value"""
        self.__size = size
        self.__position = position
        error = 'position must be a tuple of 2 positive integers'
        try:
            if position[1]:
                pass
        except IndexError:
            raise TypeError(error)

        for pos in self.__position:
            if type(pos) != int:
                raise TypeError(error)
            elif pos < 0:
                raise TypeError(error)

    @property
    def size(self):
        """ Return the size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set a new value for the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position attribute"""
        return (self.__position)

    def area(self):
        """ Compute the area of the square object"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square using the '#' character"""
        if self.__size == 0:
            print()
            return
        print('\n'*self.__position[1], end="")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end="")
            for j in range(self.__size):
                print('#', end="")
            print()
