def is_prime(n):
    if [x for x in range(2, n) if not n % x] or n <= 1:
        return False
    else:
        return True


print(is_prime(1))
