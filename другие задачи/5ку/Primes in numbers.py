def prime_factors(n):
    i = 2
    fac = []
    while i * i <= n:
        while n % i == 0:
            fac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        fac.append(int(n))
    fac = ''.join([f"({x}" + (f"**{fac.count(x)})" if fac.count(x) != 1 else ')') for x in sorted(set(fac))])
    return fac