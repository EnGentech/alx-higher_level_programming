#!/usr/bin/python3

from sys import argv

len_arg = len(argv)

if len_arg == 1:
    print("0 arguments.")
elif len_arg > 0:
    print("{:d} argument:".format(len(argv)))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
