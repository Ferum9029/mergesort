def merge(a: list, b: list) -> list:
    i = 0
    j = 0
    c = []
    # gonna kms in 3 2 1 less go
    while i != len(a) and j != len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c + (a[i:] if i != len(a) else b[j:] if j != len(b) else [])

