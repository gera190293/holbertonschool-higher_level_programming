#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

if argc == 0:
    print("0")
else:
    sum = 0
    for n in range(1, argc + 1):
        sum += int(sys.argv[n])
    print("{}".format(sum))
