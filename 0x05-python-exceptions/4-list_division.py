#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new = []
    k = 0
    j = 0
    
    for i in range(list_length):
        try:
            b =  my_list_1[i] / my_list_2[i]
        except TypeError as ex:
            new.append(0)
            print("wrong type")
        except IndexError as ex:
            new.append(0)
            print("out of range")
        except ZeroDivisionError as ex:
            new.append(0)
            print("division by 0")
        else:
            new.append(b)
        finally:
            if i == list_length:
                break
            

    return new
