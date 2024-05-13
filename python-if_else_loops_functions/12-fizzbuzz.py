#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        print("Fizz"*(n%3==0) + "Buzz"*(n%5==0) or n, end=" ")