#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        sentence = None
        return (leng, None)
    return (leng, sentence[0],)
