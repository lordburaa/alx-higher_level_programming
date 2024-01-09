#!/usr/bin/python3
""" 
    write to the file
"""
def write_file(filename="", text=""):
    """
        if the file exit overwrite the file
        and add new text to the file

        Args:

            filename: file name
            text: text to be copied
    """
    count = 0
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as k:
        read = k.readlines()
        for word in read:
            for i in range(len(word)):
                count = count + 1
    return count


