#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, item in enumerate(my_list):
        if item == 4:
            my_list[idx] = 44
    print my_list
