#!/usr/bin/python3
for i in range(1, 100):
    if (i == 99):
        print(f"{i}")
        break
    print("{:02d}, ".format(i), end="")
