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
    x is a string variable used to-
    -convert the old string into new
    """
    i = 0
    x = ""
    while i in range(len(text) - 1):
        if text[i] is '.':
            x += text[i] + chr(10) + chr(10)

        elif text[i] is '?':
            x += text[i] + chr(10) + chr(10)

        elif text[i] is ':':
            x += text[i] + chr(10) + chr(10)

        elif (text[i - 1] is '.' or
              (text[i - 1] is ':') or
              (text[i - 1] is '?') and
              text[i] is " "):

            while text[i] == " ":
                i += 1
            x += text[i]
        elif (text[i - 1] is not '.' and
              (text[i - 1] is not ':') and
              (text[i - 1] is not '?')):
                x += text[i]
        i += 1

    print("{}{}".format(x, text[-1]), end="")
