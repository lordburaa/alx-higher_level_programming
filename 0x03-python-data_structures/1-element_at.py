def element_at(my_list, idx):
    num = 0
    leng = len(my_list)
    if (idx < 0):
        return None
    if idx >= leng:   
        return None

    return my_list[idx]
    
