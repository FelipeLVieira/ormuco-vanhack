#!/usr/bin/env python
from util.util import try_float

# Method to validate if two lines are overlapping
def are_overlapping(x1, x2, x3, x4):
    x1 = try_float(x1)
    x2 = try_float(x2)
    x3 = try_float(x3)
    x4 = try_float(x4)

    if not x1 or not x2 or not x3 or not x4:
        print("Can't compare these parameters.")
        return

    if not (max(0, min(x2, x4) - max(x1, x3))):
        print("Are not overlapping")
    else:
        print("Are overlapping")
