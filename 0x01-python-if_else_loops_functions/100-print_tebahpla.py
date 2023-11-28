#!/usr/bin/python3

for i in range(122, 96, -1):
        if (i % 2 == 0):
            j = chr(i)
        else:
            j = chr(i - 32)
        print("{}".format(j), end="")
