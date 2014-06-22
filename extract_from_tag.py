# coding=utf-8
__author__ = "shyang"


def extract_from_tag(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None


s = "<test>this is a test.\nline1\nline2\nline3</test>"
print(extract_from_tag("test", s))