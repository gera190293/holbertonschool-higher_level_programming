#!/usr/bin/python3

def getUpperChar(c):
    if ord(n) >= 97 and ord(n) <= 122:
      return char(ord(n - 32))
    else:
      return c

def uppercase(str):
  for n in str:
    print("{}".format(getUpperChar(n)), end="")

  print("")