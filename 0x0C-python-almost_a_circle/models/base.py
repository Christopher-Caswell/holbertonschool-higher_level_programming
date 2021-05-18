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


import json


class Base:
    """Fragile. Don't drop"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
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
        mtfile = cls.__name__ + ".json"
        if list_objs:
            for increment in list_objs:
                mtlist.append(increment.to_dictionary())
        with open(mtfile, 'w', encoding='UTF8') as womp:
            return womp.write(cls.to_json_string(mtlist))

    @staticmethod
    def from_json_string(json_string):
        """Utilize filename to create object womp"""
        mtlist = []
        if json_string is None:
            return mtlist
        else:
            return json.loads(json_string)

#    if __name__ == '__main__':
#        unittest.main()
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
