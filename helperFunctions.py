# author   | elia deppe
# filename | helperFunctions.py

import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def is_divisible(a, b):
    return a % b == 0


def is_remainder(a, b, c):
    return a % b == c


