#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = -1 * number
    a = number % 10
    print(f"{a}", end="")
    return (a)
