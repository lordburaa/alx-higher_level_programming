def element_at(my_list, idx):
    num = 0
    leng = len(my_list)
    if (idx >= leng or idx < 0):
        return None

    new_list = my_list.pop(idx)
    return new_list
    
