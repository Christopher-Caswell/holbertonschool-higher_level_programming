#!/usr/bin/python3
"""
Write a class student that defines the student
by age, name, name, and also name
Also, retrieve a dictionary of the student with
def_to_json
"""


class Student:
    """Today, the student becomes the class. Wait, what?"""

    def __init__(self, first_name, last_name, age):
        """Public instances generated: first, last, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return all info about this moto"""
        return vars(self)
