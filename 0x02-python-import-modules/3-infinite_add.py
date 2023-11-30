#!/usr/bin/python3
import sys
sum = 0
u = len(sys.argv)
for i in range(1, u):
    sum += int(sys.argv[i])
print(f"{sum}")
