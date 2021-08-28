from math import factorial
import re


def fact(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def element(k, n, b, i):
    fc = fact(n, i) * k ** (n - i) * b ** i
    if fc == 1:
        return ''
    elif fc == -1:
        return '-'
    else:
        return str(fc)


def expand(expr):
    a = re.findall('[a-z]', expr)[0]
    expr = re.sub('-[a-z]', f"-1{a}", expr)
    coefficients = list(
        map(int, re.findall('[+-]?\d+', expr)))  # очень плохо знаю регулярные выражения, поэтому так написал
    if len(coefficients) == 2: coefficients = [1] + coefficients
    k, b, n = coefficients
    s = [element(k, n, b, i) + f"{a}^{n - i}" for i in range(n + 1)]
    if s[-1] == f'{a}^0':
        s[-1] = '1'
    elif s[-1] == f'-{a}^0':
        s[-1] = '-1'
    else:
        s[-1] = s[-1][:-3]
    return '+'.join(s).replace(f"{a}^1", a).replace('+-', '-')
