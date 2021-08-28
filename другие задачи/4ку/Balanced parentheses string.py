def balanced_parens(n, k):
    try:
        return sorted(n)[k]
    except:
        return None

print(balanced_parens(["()()","(())"],1))