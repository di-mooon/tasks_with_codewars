import numpy as np


def spiralize(size):
    matrix = np.random.randint(1, 2, (size, size))
    for i in range(1, size, 2):
        matrix[i][i - 1:-i] = [0 for _ in matrix[i][i - 1:-i]]
        matrix[::-1][i][i:-i] = [0 for _ in matrix[::-1][i][i:-i]]
        matrix[:, i][i + 2:-i - 1] = [0 for _ in matrix[:, i][i + 2:-i - 1]]
        matrix[:, -i - 1][i:-i] = [0 for _ in matrix[:, -i:-1][i:-i]]
    return matrix.tolist()


