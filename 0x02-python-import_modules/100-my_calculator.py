#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]
    args_len = len(args)
    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(args[0])
        op = args[1]
        b = int(args[2])
        if op == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif op == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    pass


if __name__ == '__main__':
    main()
