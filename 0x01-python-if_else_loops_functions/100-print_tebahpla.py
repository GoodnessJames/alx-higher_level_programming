#!/usr/bin/python3
for i in range(122, 96, -2):
    letters = f"{chr(i):s}{chr(i + ord('A') - ord('a') - 1):s}"
    print("{:s}".format(letters), end="")
