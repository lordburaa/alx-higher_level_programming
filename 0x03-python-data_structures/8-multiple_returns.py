#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if (leng == 0):
        sentence[0] = None
    return (leng, sentence[0])
