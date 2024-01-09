#!/usr/bin/python3
"""
    json

"""

import json


def from_json_string(my_str):
    """
        decoding from the file
    """
    new_str = json.loads(my_str)
    return new_str
