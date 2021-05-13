#!/usr/bin/python3
"""
Write a function that creates an Object from a JSON file:
no exceptions necessary to handle
no file permissions either
"""
from sys import argv
"""Access argv functions"""
savejson = __import__('5-save_to_json_file').save_to_json_file
"""write object to string, JSON style"""
loadjson = __import__('6-load_from_json_file').load_from_json_file
"""write object from JSON string"""

add_item = "add_item.json"
"""file name to return no matter what"""

try:
    result = loadjson(add_item)
    """It won't run if it isn't there. Woof. Brain pain"""
except:
    result = []
    """List created for storage"""
for x in range(1, len(argv)):
    result.append(argv[x])
savejson(result, add_item)
