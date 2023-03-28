#!/usr/bin/python3
"""define a class for a square and checkmate
using int and tuple"""


class Square:
    """define a class of square with a check
    for int and tuple which will return area of
    a square and prints # is a certain order"""

    def __init__(self, size=0, position=(0, 0)):
        """define and initialize size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """return the value as getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """check for type of data and set value"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of a square"""
        ans = self.__size**2
        return ans

    def my_print(self):
        """Print # in a certain order
        """
        if self.size:
            print('\n' * self.position[1], end="")
            print('\n'.join(
                [' ' * self.position[0] + '#' * self.size] * self.size
            ))
        else:
            print()
