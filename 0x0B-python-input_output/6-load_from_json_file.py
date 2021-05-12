#!/usr/bin/python3
"""
Write a function that creates an Object from a JSON file:
no exceptions necessary to handle
no file permissions either
"""

import json


def load_from_json_file(filename):
    """Utilize filename to create object womp"""
    with open(filename, encoding='UTF8') as womp:
        return json.loads(womp.read())
