#!/usr/bin/env python
from util.util import try_float


# Method to receive two inputs, try to parse to a decimal number
# and compare them, returning
def which_is_greater(input1, input2):
    input1_float = try_float(input1)
    input2_float = try_float(input2)

    if not input1_float or not input1_float:
        print("Can't compare these parameters.")
        return

    if input1_float > input2_float:
        return print(input1_float, " is greater")
    elif input2_float > input1_float:
        return print(input2_float, " is greater")
    else:
        return print("Both numbers are equal")
