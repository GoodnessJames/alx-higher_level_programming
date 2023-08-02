#!/usr/bin/python3
# 2-square.py
"""A class that defines a square based on 1-square.py."""


class Square:
    """Class Square method definition."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
