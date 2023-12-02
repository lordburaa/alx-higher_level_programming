#!/ust/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0):
        return (my_list)
    if (idx >= len(my_list)):
        return (my_list)
    new_list = my_list
    k = 0
    del my_list[idx]
    for i in range(len(my_list)):
        if (idx == i):
            continue
        else:
            new_list[k] = my_list[i]
            k += 1
    return new_list
