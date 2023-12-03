#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    file = dir(hidden_4)
    leng = len(file)
    for i in range(leng):
        if (file[i][0:2] != "__"):
            print(file[i])
