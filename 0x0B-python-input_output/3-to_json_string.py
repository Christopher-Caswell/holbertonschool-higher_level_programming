#!/usr/bin/python3
import json
"""
Write a function that returns
the JSON representation of an object (string):
No need to manage exceptions
"""


def to_json_string(my_obj):
    """return json string"""
    return json.dumps(my_obj)
