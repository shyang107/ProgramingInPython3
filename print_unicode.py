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

# if word != 0:
# print_unicode_table(word)

print("\n\nThe CJK compatibility unicode table")


def get_line(column, columns, fmt, head, line, split):
    while column < columns:
        line += fmt.format(head) + split
        column += 1
    return line


def print_cjk_unicode_table():
    columns = 12
    width = 7
    split = " "
    column = 0
    head1 = "char/uc"
    head2 = "-" * width
    fmt = "{0:^" + str(width) + "}"
    line1 = ""
    line2 = ""
    line1 = get_line(column, columns, fmt, head1, line1, split)
    line2 = get_line(column, columns, fmt, head2, line2, split)
    print(line1)
    print(line2)

    code = ord(" ")
    end = sys.maxunicode

    column = 0
    line1 = ""
    line2 = ""
    line3 = ""
    rows = 10
    row = 0
    fmtc = "  {0} "
    while code < end and row < rows:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        cc = str(c).center(width, '*')
        if "cjk" in name.lower():
            if column < columns:
                line1 += fmt.format(cc) + split
                line2 += fmt.format(str(code)) + split
                line3 += fmt.format(str(len(c))) + split
                column += 1
            else:
                print(line1)
                print(line3)
                print(line2)
                line1, line2, column = "", "", 0
                row, line3 = row + 1, ""
        code += 1


print_cjk_unicode_table()
