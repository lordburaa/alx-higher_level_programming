#!/usr/bin/python3
if __name__ = "__name__"
    import sys
temp = int(0)
summ = bin(0)
u = len(sys.argv)
for i in range(1, u):
    temp = temp + int(sys.argv[i])
    summ = bin(temp) or summ

print("{}".format((int(summ, 2))))
