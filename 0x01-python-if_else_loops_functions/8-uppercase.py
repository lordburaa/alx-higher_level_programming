#!/uar/bin/python3
def uppercase(str):
    for i in str(str):
        if (ord(i) > 97 and ord(i) < 122):
            j = chr(ord(i) - 32)
            print("{:c}".format(j), end="")
        else:
            print("{:c}".format(i), end="")
