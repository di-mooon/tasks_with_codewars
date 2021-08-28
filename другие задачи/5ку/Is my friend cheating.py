import math


def remove_nb(n):
    s = (sum(range(n + 1)) + 1)
    lst = [
        (x - 1, s // x - 1)
        for x in range(1, int(math.sqrt(s)) + 1)
        if not s % x and (x in range(n) and s // x in range(n))
    ]
    return lst + [x[::-1] for x in lst[::-1]]
