#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    fl = dir(hidden_4)
    leng = len(fl)
    for i in range(leng):
        if (fl[i][0:2] != "__"):
             print(fl[i])
