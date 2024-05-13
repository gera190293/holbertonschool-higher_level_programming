#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        firstchar = None
    else:
        firstchar = sentence[0]
    new_tuple = (length, firstchar)
    return new_tuple
