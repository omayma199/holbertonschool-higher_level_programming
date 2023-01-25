#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)

    sum = ((tuple_a[0] if i > 0 else 0) + (tuple_b[0] if j > 0 else 0),
        (tuple_a[1] if i > 1 else 0) + (tuple_b[1] if j > 1 else 0))

    return sum
