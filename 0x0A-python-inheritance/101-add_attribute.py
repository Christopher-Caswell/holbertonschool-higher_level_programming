#!/usr/bin/python3
"""
Write a function that adds a new attr to
an object if it's possible
Not allowed to Try/Catch
"""


def add_attribute(obj, attribute, value):
    """Decipher if obj is builtin and listed in slots"""
    if obj.__class__.__module__ == 'builtins':
        """If module contains class of builtins"""
        """Module is name of file containing call"""
        raise TypeError('can\'t add new attribute')
    if hasattr(obj, '__slots__'):
        if attribute in obj.__slots__:
            """slots is list of all permitted attr"""
            add_attribute(obj, attribute, value)
            return
        else:
            raise TypeError('can\'t add new attribute')
    setattr(obj, attribute, value)
