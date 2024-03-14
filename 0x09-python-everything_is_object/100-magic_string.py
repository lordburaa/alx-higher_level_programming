#!/usr/bin/python3
def magic_string():
    magic_string.count += 1

    for i in range(magic_string.count):
        print("hello", end=",")
    print()
magic_string.count = 0
