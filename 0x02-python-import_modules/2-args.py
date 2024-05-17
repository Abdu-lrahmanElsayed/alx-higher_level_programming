#!/usr/bin/python3
def main():
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        print("0 arguments.")
    elif len(args) == 1:
        print("1 argument:")
        for arg in range(len(args)):
            print("1: {:s}".format(args[arg]))
    else:
        print("{:d} arguments:".format(len(args)))
        for arg in range(len(args)):
            print("{:d}: {:s}".format(arg, args[arg]))
    pass


if __name__ == '__main__':
    main()
