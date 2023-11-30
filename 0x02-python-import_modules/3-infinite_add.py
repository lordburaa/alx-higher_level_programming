#!/usr/bin/python3
if __name__ == "__main__":
    import sys
temp = int(0)
summ = bin(0)
u = len(sys.argv)
if u != 2:
    for i in range(1, u):
        temp = temp + int(sys.argv[i])
        summ = bin(temp) or summ
else:
    summ += bin(temp)
print("{}".format((int(summ, 2))))
