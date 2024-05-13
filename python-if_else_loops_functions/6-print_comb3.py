#!/usr/bin/python3
for m in range(1, 10):
    for n in range(m, 10):
        if m < 9:
            print("{}{}, ".format(m - 1, n), end="")
        else:
            print("{}{}".format(m - 1, n))
