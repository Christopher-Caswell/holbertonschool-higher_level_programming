#!/usr/bin/python3
"""
Write a function that writes an Object to a text file
using a JSON representation:
no need to manage exceptions or file permissions
"""

import json


def save_to_json_file(my_obj, filename):
    """Save obj to filename"""
    with open(filename, 'w', encoding='UTF8') as womp:
        return womp.write(json.dumps(my_obj))
