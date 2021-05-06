#!/usr/bin/python3
"""
Print a pair of new lines between the strings
separators are . ? :
raise a flag if not a string, though
"""


def text_indentation(text):
    """Consider me noted"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    """
    chr(10) is a new line.
    Written in ASCII to keep clean
    and somewhat save space for pep8
    """
    # r = ""
    x = ""
    for i in range(len(text) - 1):
        if text[i] is chr(46):
            """chr(46) = '.'"""
            x += text[i] + chr(10) + chr(10)
        elif text[i] is chr(63):
            """chr(63) = '?'"""
            x += text[i] + chr(10) + chr(10)
        elif text[i] is chr(58):
            """chr(58) = ':'"""
            x += text[i] + chr(10) + chr(10)
        else:
            if (text[i - 1] is not chr(46)) and\
                    (text[i - 1] is not chr(63)) and\
                    (text[i - 1] is not chr(58)):
                x += text[i]
    print("{}".format(x))
