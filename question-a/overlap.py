def are_overlapping(x1, x2, x3, x4):
    if not(x1 < x4 and x3 < x2):
        print("Are not overlapping")
    else:
        print("Are overlapping")
