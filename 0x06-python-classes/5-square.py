#!/usr/bin/python3
"""
a class of square with an expression of getter
and setter
"""


class Square:
    "defining a private instance attribute"""
    __size = None

    def __init__(self, size=0):
        """initializing data input"""
        self.__size = size

    @property
    def size(self):
        """setting the getter property"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting and checking data type on user input"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """return area of a square"""
        ans = self.__size**2
        return ans

    def my_print(self):
        """print an equal value matrix using #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
