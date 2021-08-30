def is_divisible_by_6(string):
    lst = []
    for x in range(int('9' * string.count("*"))+1):
        a = string
        for i in list(str(x).zfill(string.count("*"))):
            a = a.replace('*', i, 1)
        if not int(a) % 6: lst.append(a)
    return lst

