def sol_equa(n):
    lst = []
    for k in [(x, n // x) for x in range(1, int(n ** (1 / 2)) + 1) if n % x == 0]:
        y = (k[0] - k[1]) / -4
        x = k[1] - 2 * y
        if str(x)[str(x).find('.') + 1] and str(y)[str(y).find('.') + 1] == '0':
            lst.append([int(x), int(y)])
    return lst
