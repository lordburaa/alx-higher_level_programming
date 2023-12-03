#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
