#!/usr/bin/python3
import sys
u = len(sys.argv)
if (u == 2):
    print(f"{u - 1} argument")
else:
    print(f"{u - 1} arguments:")
for i in range(1, u):
    print("{}: {}".format(i, sys.argv[i]))
