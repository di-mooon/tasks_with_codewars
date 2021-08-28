def prim_fac(n):
    i = 2
    prim_fac = []
    while i * i <= abs(n):
        while abs(n) % i == 0:
            prim_fac.append(i)
            n = abs(n) // i
        i = i + 1
    if abs(n) > 1:
        prim_fac.append(abs(n))
    return prim_fac


def sum_for_list(lst):
    set_prim_fac = sorted(set([k for x in lst for k in prim_fac(x)]))
    return [[pr_fc, sum([i for i in lst if not i % pr_fc])] for pr_fc in set_prim_fac]