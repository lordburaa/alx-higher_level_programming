#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        if (ord(i) >= 97 and ord(i) <= 122):
            i = int(ord(i) - 32)
            i = chr(i)
#          print("{}".format(chr(j)), end="")
        else:
            i = int(ord(i))
            i = chr(i)
        print("{}".format(i), end="")
    print()
