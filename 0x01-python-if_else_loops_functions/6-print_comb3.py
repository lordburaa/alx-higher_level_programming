#!/usr/bin/python3
for i in range(0, 9):
    j = i
    for j in range(j, 9):
        print("{}{}".format(i, j + 1), end="")
        if (--i != 8 and --j != 9):
            print(", ", end="")
print()
