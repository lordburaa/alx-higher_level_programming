#!/usr/bin/python3
"""
    json
"""


import json


def save_to_json_file(my_obj, filename):
    """ daving json format """

    form = json.dumps(my_obj)

    with open(filename, 'w+', encoding="utf-8") as f:
        return f.write(form)
