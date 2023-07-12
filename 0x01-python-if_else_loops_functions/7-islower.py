#!/usr/bin/python3
# File: 7-islower.py


def islower(c):
    """A function that checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
