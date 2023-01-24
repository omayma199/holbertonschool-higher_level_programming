#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = list(my_string)
        for i in new_string:
            if i in "cC":
                new_string.remove(i)
        my_string = "".join(new_string)
    return my_string
