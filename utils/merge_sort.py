def merge(a: list, b: list) -> list:
    # scope indexes of a and b
    i, j = 0, 0
    c = []

    # adding values from a and b to c in ascending order
    while i != len(a) and j != len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # returning c and the rest of values if not all elements are in c
    return c + (a[i:] if i != len(a) else b[j:])

