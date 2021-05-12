#!/usr/bin/python3
"""
Write a function that returns an object
(Python data structure) represented by a JSON string:
No need to manage exceptions
"""

import json


def from_json_string(my_str):
    """return json obj"""
    return json.loads(my_str)
