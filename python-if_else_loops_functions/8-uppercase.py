#!/usr/bin/python3

def getUpperChar(c):
    if ord(c) >= 97 and ord(c) <= 122:
      return ord(c - 32)
    else:
      return c

def uppercase(str):
  for n in str:
    print("{}".format(getUpperChar(n)), end="")

  print("")