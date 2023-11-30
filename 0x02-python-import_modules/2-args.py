#!/usr/bin/python3
if __name__ == "__main__":
    import sys
u = len(sys.argv)
if (u == 1):
    print(f"{u - 1} arguments.")
else:
    if u == 2:
        print(f"{u - 1} argument.")
    else:
        print(f"{u - 1} arguments:")
    for i in range(1, u):
        print("{}: {}".format(i, sys.argv[i]))
