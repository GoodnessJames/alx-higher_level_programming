#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if my_list is None:
        return

    for i in my_list[::-1]:
        print("{:d}".format(my_list[i - 1]))
        i -= 1
