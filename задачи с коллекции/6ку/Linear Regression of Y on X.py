def regressionLine(x, y):
    ex2 = sum(map(lambda x: x ** 2, x))
    exy = sum([i * j for i, j in zip(x, y)])
    a = (ex2 * sum(y) - sum(x) * exy) / (len(x) * ex2 - sum(x) ** 2)
    b = (len(x) * exy - sum(x) * sum(y)) / (len(x) * ex2 - sum(x) ** 2)
    return round(a, 4), round(b, 4)


print(regressionLine([25, 30, 35, 40, 45, 50], [78, 70, 65, 58, 48, 42]))
