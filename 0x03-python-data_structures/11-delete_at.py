#!/ust/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list
    if (idx < 0):
        return (new_list)
    if (idx >= len(my_list)):
        return (new_list)
    
    k = 0
    del new_list[idx]
    
    return new_list
