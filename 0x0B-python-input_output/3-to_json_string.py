#!/usr/bin/python3
"""
    checking

"""


import json


def to_json_string(my_obj):
    """ json format
    """
    new_list = json.dumps(my_obj)
    return new_list
