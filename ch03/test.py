# coding=UTF-8
__author__ = 'shyang'

codes = []
for sex in "MF":  # Male, Female
    for size in "SMLX":  # Small, Medium, Large, eXtra large
        if sex == "F" and size == "X":
            continue
        for color in "BGW":  # Black, Gray, White
            codes.append(sex + size + color)
print(len(codes), codes)

codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW" if not (s == "F" and z == "X")]
print(len(codes), codes)

