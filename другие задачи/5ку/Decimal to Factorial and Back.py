from math import factorial
import string as  st


def dec_2_fact_string(nb):
    i = 1
    string = ''
    while nb > 0:
        string += str(nb % i) if nb % i < 10 else st.ascii_lowercase[nb % i - 10]
        nb //= i
        i += 1
    return string[::-1].upper()


def fact_string_2_dec(string):
    string = sum([((ord(j) - 87) if j.isalpha() else int(j)) * factorial(i)
                  for i, j in enumerate(string.lower()[::-1])])
    return string
