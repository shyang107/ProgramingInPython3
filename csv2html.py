# coding=UTF-8
__author__ = 'shyang'

import sys


"""
command: csv2html.py < data/co2-sample.csv > co2-sample.htm
"""

# co2-sample.csv will have contents similar to this:
# "COUNTRY","2000","2001",2002,2003,2004 ...
# "ANTIGUA AND BARBUDA",0,0,0,0,0 ...
# "ARGENTINA",37,35,33,36,39 ...
# "BAHAMAS, THE",1,1,1,1,1 ...
# "BAHRAIN",5,6,6,6,6 ...
# ...

# co2-sample.html will have contents similar to this:
# <table border='1'><tr bgcolor='lightgreen'>
#     <td>Country</td><td align='right'>2000</td><td align='right'>2001</td>
#     <td align='right'>2002</td><td align='right'>2003</td>
#     <td align='right'>2004</td></tr>
#     ...
#     <tr bgcolor='lightyellow'><td>Argentina</td>
#     <td align='right'>37</td><td align='right'>35</td>
#     <td align='right'>33</td><td align='right'>36</td>
#     <td align='right'>39</td></tr>
#     ...
#     </table>

def printStart():
    print("<table border ='1'>")


def printEnd():
    print("</table>")


def extractFields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c  # other quote inside quoting string
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c  # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escapeHtml(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt")
    text = text.replace(">", "&gt;")
    return text


def printLine(line, bgColor, maxWidth):
    print("<tr bgcolor='{0}'>".format(bgColor))
    fields = extractFields(line)
    for field in fields:
        if field is None:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxWidth:
                    field = escapeHtml(field)
                else:
                    field = "{0} ...".format(escapeHtml(field[:maxWidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def main():
    maxWidth = 100
    printStart()
    rowCount = 0
    while True:
        try:
            line = input()
            if rowCount == 0:
                bgColor = "lightgreen"
            elif rowCount % 2 == 0:
                bgColor = "white"
            else:
                bgColor = "lightyellow"
            printLine(line, bgColor, maxWidth)
            rowCount += 1
        except EOFError:
            break
    printEnd()


main()
