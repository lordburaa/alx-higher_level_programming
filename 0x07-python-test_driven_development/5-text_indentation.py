#!/usr/bin/python3
"""
Function containg that indentstexts

"""


def text_indentation(text):
    """ Function prints a tezt iwht new line  after each ',', '?' and ':'

    Args:
        text (str): the string to be printed


    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1

