# coding=utf-8
__author__ = 'shyang'

import sys
import unicodedata


def print_unicode_table(word):
    """
    print unicode table
    :param word: None for all unicode; unicodes with name including "word"
    """
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")  # ord(): represent the unicode code point of a character, and it is the inverse of chr()
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))
        code += 1


"""
example: print_unicode.py spoked
"""
word = None
if len(sys.argv) > 1:
    if (sys.argv[1]) in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        word = 0
    else:
        word = sys.argv[1].lower()

if word != 0:
    print_unicode_table(word)

