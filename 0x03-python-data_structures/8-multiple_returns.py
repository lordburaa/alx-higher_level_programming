#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    temp = sentence.split() + ["he"]
    if (sentence == ""):
        temp[0] = None
    return (leng, temp[0][0])
