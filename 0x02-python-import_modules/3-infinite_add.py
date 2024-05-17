#!/usr/bin/python3
def main():
    import sys
    args = sys.argv[1:]
    length = len(args) - 1
    addition = 0
    if len(args) == 0:
        print("0")
    elif len(args) == 1:
        for arg in args:
            print(arg)
    else:
        for arg in args:
            addition += int(arg)
        print(addition)


if __name__ == "__main__":
    main()
