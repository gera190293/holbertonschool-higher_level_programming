#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
elif number % 10 > 5 and number > 0:
    print(f"Last digit of {number} is {number%10} and is greater than 5")
else:
    n = abs(number)
    print(f"Last digit of {-n} is {-(n % 10)} and is less than 6 and not 0")
