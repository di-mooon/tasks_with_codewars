def is_divisible_by_6(s):
    return [str(int(s.replace('*', f"{x}"))) for x in range(10) if not int(s.replace('*', f"{x}")) % 6]



