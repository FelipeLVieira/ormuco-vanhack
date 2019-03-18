from decimal import *


def which_is_greater(input1, input2):
    input1_dec = try_decimal(input1)
    input2_dec = try_decimal(input2)

    if input1_dec > input2_dec:
        return input1_dec
    elif input2_dec < input1_dec:
        return input2_dec
    else:
        return input1_dec


def try_decimal(value):
    try:
        return Decimal(value)
    except ValueError:
        return value