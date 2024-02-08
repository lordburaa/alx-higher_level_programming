#!/usr/bin/python3
"""
    json
"""

import json


def load_from_json_file(filename):
    with open(filename) as f:
        new_str = json.load(f)
        return new_str
