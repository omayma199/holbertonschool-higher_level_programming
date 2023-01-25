#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    while my_list != []:
        try:
            print(next(my_list))
        except StopIteration:
            print()
            break
        x += 1