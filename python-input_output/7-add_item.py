#!/usr/bin/python3
"""
function that writes Python obj to file using JSON represenation
"""


def save_to_json_file(my_obj, filename):
    """
    Writes Python obj to file using JSON represenation
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
