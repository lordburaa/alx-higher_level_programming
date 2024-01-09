#!/usr/bin/python3
""" scripts for the json """


import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    new = []
    with open('add_item.json', 'w') as f:
        pass
    new = load_from_json_file('add_item.json')
    new += sys.argv[:-1]

    save_to_json_file(new, 'add_item.json')
