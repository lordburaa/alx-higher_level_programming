#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in (dir(hidden_4)):
        if (ord(i[1]) != ord('_')):
             print(f"{i}")
