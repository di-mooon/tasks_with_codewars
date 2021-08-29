from math import factorial


def recursive_list_position(s):
    if len(s) < 2: return 0
    lst = sorted(s[:])
    a = 1
    for i, j in enumerate(lst):
        n = 1
        while i + n < len(lst) and lst[i + n] == j:
            n += 1
        a *= n
    position = lst.index(s[0])
    return factorial(len(s) - 1) * position // a + recursive_list_position(s[1:])


def list_position(s):
    return recursive_list_position(list(s)) + 1

