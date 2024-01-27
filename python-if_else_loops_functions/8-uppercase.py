#!/usr/bin/python3

def getUpperChar(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr(ord(c) - 32)
    else:
<<<<<<< HEAD
        return c        
    def uppercase(str):
        for n in str:
            print("{}".format(getUpperChar(n)), end="")
        print("")
=======
        return c
    
def uppercase(str):
    for n in str:
        print("{}".format(getUpperChar(n)), end="")
    print("")
    
>>>>>>> 130734a820bbbf0beba8a576f0fc6dff7a031b3c
