#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
k = int(0)
u = len(sys.argv) - 1
if (u != 3):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
operator = {'+', '-', '*', '/'}
for i in operator:
    if (i == sys.argv[2]):
        k = 2 + k
        break
    k += 1
if (k == 4):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
k = k - 2
fun = [calculator_1.add, calculator_1.sub, calculator_1.mul, calculator_1.div]
print("{} {} {} = {}".format(int(sys.argv[1]), chr(sys.argv[2]), int(sys.argv[3]),
                             int(fun[k](int(sys.argv[1]), int(sys.argv[3])))))
