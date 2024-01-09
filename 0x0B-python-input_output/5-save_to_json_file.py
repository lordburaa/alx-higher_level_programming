#!/usr/bin/python3
"""
    json
"""


import json


def save_to_json_file(my_obj, filename):
    """ daving json format """

    with open(filename, 'a+', encoding="utf-8") as f:
        json.dump(my_obj, f)
