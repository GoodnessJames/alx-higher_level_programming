#!/usr/bin/python3
# 12-roman_to_int.py


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if type(roman_string != str) or roman_string is None:
        return (0)

    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0

    for i in range(len(roman_string)):
        if values.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                values[roman_string[i]] < values[roman_string[i + 1]]):
            num += values[roman_string[i]] * -1
        else:
            num += values[roman_string[i]]
    return (num)
