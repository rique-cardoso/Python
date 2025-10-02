from typing import Callable

Matrix = list[list[int]]

def make_matrix(n: int, m: int, entry_fn: Callable[[int, int], int]) -> Matrix:
    '''Retorna uma matriz n x m onde cada elemento é definido pela função entry_fn(i, j)'''
    return [[entry_fn(i, j) for j in range(m)] for i in range(n)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

def sum_matrix(n: int, m: int) -> Matrix:
    return make_matrix(n, m, lambda i, j: i + j)

# print(identity_matrix(4))
# [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 1, 0],
#  [0, 0, 0, 1]]

print(sum_matrix(3, 5))
# [[0, 1, 2],
#  [1, 2, 3],
#  [2, 3, 4]]
