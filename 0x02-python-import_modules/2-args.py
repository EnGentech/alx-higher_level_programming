#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    len_arg = len(argv)

    if len_arg == 1:
        print("0 arguments.")
    elif len_arg == 2:
        print("{:d} argument:".format(len(argv) - 1))
        print("{:d}: {}".format(1, argv[1]))
    elif len_arg > 2:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
           print("{:d}: {}".format(i, argv[i]))
