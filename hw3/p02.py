import math

def func(_l1, _l2):
    l1 = _l1 + [math.inf]
    l2 = _l2 + [math.inf]
    merged = []
    i = 0
    j = 0
    while (i + j) < (len(l1) + len(l2) - 2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    return merged