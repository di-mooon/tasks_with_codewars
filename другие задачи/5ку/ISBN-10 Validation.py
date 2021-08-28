def valid_ISBN10(isbn):
    try:
        return not (sum([(i + 1) * int(j) for i, j in enumerate(isbn[:-1])] +
                    [(int(isbn[9]) if isbn[9].isdigit() else 10) * 10]) % 11)
    except:
        return False

