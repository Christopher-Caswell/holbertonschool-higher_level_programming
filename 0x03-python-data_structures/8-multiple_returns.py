#!/usr/bin/python3
def multiple_returns(sentence):
    x = tuple()
    if len(sentence) == None:
        x = (0, None)
    else:
        x = (len(sentence), sentence[0])
    return x
