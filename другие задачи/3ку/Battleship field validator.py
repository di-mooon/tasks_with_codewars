import numpy as np


# можно было бы и лучше, но это работает

def find_ships(field):
    lst = []
    lst2 = []
    for row in range(12):
        for col in range(12):
            if field[row][col] == 1 \
                    and (field[row + 1][col] == 0 or field[row + 1][col] == 2) \
                    and (field[row - 1][col] == 0 or field[row - 1][col] == 2) \
                    and (field[row - 1][col - 1] == 0 or field[row - 1][col - 1] == 2) \
                    and (field[row - 1][col + 1] == 0 or field[row - 1][col + 1] == 2) \
                    and (field[row + 1][col + 1] == 0 or field[row + 1][col + 1] == 2) \
                    and (field[row + 1][col - 1] == 0 or field[row + 1][col - 1] == 2):
                lst2.append(field[row, col])
            else:
                lst.append(lst2) if lst2 else None
                lst2 = []
    return lst


def validate_battlefield(field):
    correct_lst = [1] * 8 + [2, 2, 2, 3, 3, 4]
    field = np.array([[2] * 12] + [[2] + x + [2] for x in field] + [[2] * 12])
    return sorted([len(ships) for ships in (find_ships(field) + find_ships(field.T))]) == correct_lst


print(validate_battlefield([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                            [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], ]))
