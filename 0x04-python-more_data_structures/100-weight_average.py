#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    totalW = 0
    totalS = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        totalW += weight
        totalS += score * weight
    return totalS / totalW
