#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ctr = 0
    for i in range(0, x):
        try:
            print(next(my_list))
            ctr = ctr + 1
        except IndexError:
            break
    print()
    return ctr