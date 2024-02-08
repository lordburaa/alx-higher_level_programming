#!/usr/bin/python3
"""
    json
"""

import json


def load_from_json_file(filename):
    """create an object from  JSON  file"""
    with open(filename, "r") as f:
        new_str = json.load(f)
        return new_str
