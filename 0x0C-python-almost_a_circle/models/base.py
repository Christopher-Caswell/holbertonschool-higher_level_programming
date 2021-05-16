#!/usr/bin/python3
"""
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)
-
if id is not None, assign the public instance
attribute id with this argument value
-
you can assume id is an integer and you
don’t need to test the type of it
-
otherwise, increment __nb_objects and assign the new value
to the public instance attribute id
"""


class Base:
    """Fragile. Don't drop"""

    def __init__(self, id=None):
        __nb_objects = 0
        if id is None:
            __nb_objects += 1
            id = __nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list_objs to json string"""
        mtlist = []
        if list_objs is None:
            return mtlist
        with open(filename, 'w', encoding='UTF8') as womp:
            return womp.write(json.dumps(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Utilize filename to create object womp"""
        mtlist = []
        if json_string is None:
            return mtlist
        with open(filename, encoding='UTF8') as womp:
            return json.loads(json_string)
"""
@classmethod
def load_from_file(cls):
-Returns a list of instances-
itemx = cls.__name__ + ".json"
try:
result = loadjson(itemx)
except:
savejson(result, itemx)
"""