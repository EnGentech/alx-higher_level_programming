#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    add = 0
    
    if argv_len == 1:
        print('0')
    elif argv_len > 1:
        for i in range(len(argv) - 1):
            add += int(argv[i + 1])
        print(add)
