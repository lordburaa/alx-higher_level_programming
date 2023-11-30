#!/usr/bin/python3
import sys
u = len(sys.argv)
print(f"{u - 1} argument:")
for i in range(1, u):
    print("{}: {}".format(i, sys.argv[i]))
