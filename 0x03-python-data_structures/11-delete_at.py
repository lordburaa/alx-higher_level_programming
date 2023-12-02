#!/ust/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    k = 0
    if (idx < 0):
        return (new_list)
    if (idx >= len(my_list)):
        return (new_list)
    for i in range(len(my_list)):
        if i != idx:
            new_list[k] = my_list[i]
            k += 1
    
    z = my_list[idx]
    my_list.remove(z)
    new_list = my_list
    return new_list
