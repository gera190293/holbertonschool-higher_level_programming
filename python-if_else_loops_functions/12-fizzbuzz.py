#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 100):
        if (n%3 == 0 and n%5 != 0):
            print("Fizz ", end="")
        elif (n%3 != 0 and n%5 == 0):
            print("Fuzz ", end="")
        elif (n%3 == 0 and n%5 == 0):
            print("FizzFuzz ", end="")
        else:
            print("{} ".format(n), end="")
