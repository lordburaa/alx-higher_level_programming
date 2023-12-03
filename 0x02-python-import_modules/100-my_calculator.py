#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    l = 0
    leng = len(argv[2])
    if (leng == 1):
        a = int(argv[1])
        b = int(argv[3])
        if operator == "+":
            l = 1
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == "-":
            l = 1
            print("{:d} - {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == "*":
            l = 1
            print("{:d} * {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == "/":
            l = 1
            print("{:d} / {:d} = {:d}".format(a, b, add(a, b)))
    if (l == 0):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
