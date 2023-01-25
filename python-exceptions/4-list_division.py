#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    New_list = []
    counter = 0
    for a in range(list_length):
        try:
            counter = my_list_1[a] / my_list_2[a]
        except(ValueError, TypeError):
            print("wrong type")
            counter = 0
        except ZeroDivisionError:
            print("division by 0")
            counter = 0
        except IndexError:
            print("out of range")
            counter = 0
        finally:
            New_list.append(count)
    return New_list
