#!/usr/bin/python3
def print_list_integer(my_list=[])
{
    print(*my_list, sep = "\n".join('{:d}' for _ in range(len(my_list))).format(*my_list)
}
