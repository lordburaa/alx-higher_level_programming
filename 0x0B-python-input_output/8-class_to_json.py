#!/usr/bin/python3
"""
    class json
"""

import json


def class_to_json(obj):
    """ function retnrs thedictionary description with simple data structure"""

    return obj.__dict__
