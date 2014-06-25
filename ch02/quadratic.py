# coding=UTF-8
__author__ = 'shyang'

import math
import cmath
import sys

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed!")
                x = None
        except ValueError as err:
            print(err)
    return x


a = get_float("enter a = ", False)
b = get_float("enter b = ", True)
c = get_float("enter c = ", True)

x1, x2 = None, None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:  # discriminant < 0
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

equation = "{a}x\N{SUPERSCRIPT TWO} {b:+}x {c:+} = 0 \N{RIGHTWARDS ARROW} x = {x1:.3f}".format(**locals())
if x2 is not None:
    equation += " or x = {x2:.3f}".format(**locals())
print(equation)