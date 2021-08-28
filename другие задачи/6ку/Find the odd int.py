def find_it(seq):
    for integer in set(seq):
        if seq.count(integer) % 2 == 1:
            return integer