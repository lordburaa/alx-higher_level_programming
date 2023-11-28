#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digt of {number} is {abs(number) % 10} ater than 5" if (number % 10) >= 5 else f"Last dgigit of {number} is {abs(number) % 10} and is 0" if (number % 10) == 0 else f"Last digit of {number} is {abs(number)% 10} and is less than 6 and not 0")
