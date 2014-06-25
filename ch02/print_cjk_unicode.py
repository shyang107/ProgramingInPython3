# coding=utf-8
__author__ = 'shyang'

import sys
import unicodedata


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


print("\n\nThe CJK compatibility unicode table")
print_cjk_unicode_table()
