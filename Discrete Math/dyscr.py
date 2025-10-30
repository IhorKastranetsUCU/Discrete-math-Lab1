"""
Module for working with binary relation matrices: reading/writing CSV, computing reflexive, symmetric,
and transitive closures, checking transitivity, and finding equivalence relations.

Authors: Ihor Kastranets and Vitali Volodskyi
"""

from copy import deepcopy

def read_matrix(file: str) -> list:
    """
    This function reads a matrix from a CSV file where each row contains digits without separators (e.g., "0101").
    Each line in the CSV file represents one row of the matrix.

    :param file: path to the CSV file containing the matrix
    :return matrix: list of lists
    """
    matrix = []
    with open(file, "r") as f:
        for line in f.readlines():
            matrix.append([int(x) for x in line.strip()])
    return matrix


def write_relation(filename: str, matrix: list) -> None:
    """
    This function writes a matrix to a CSV file where each row is saved as a single string.
    If the file does not exist, it will be created automatically.
    If the file already exists, its previous content will be completely overwritten.

    :param matrix: list of lists representing the relation matrix
    :param filename: name of the file to write to
    :return: None
    """
    with open(filename, 'w') as file:
        for row in matrix:
            line = "".join(str(el) for el in row)
            print(line)
            file.write(line + "\n")


def reflexive_closure(matrix: list) -> list:
    """
    This function computes the reflexive closure of a given relation matrix.
    It makes each element on main diagonal value 1.

    :param matrix: list of lists representing the relation matrix
    :return matrix: with reflexive closure

    >>> reflexive_closure([[0,1,0],[0,0,1],[0,0,0]])
    [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
    """
    matrix = deepcopy(matrix)
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix


def symmetric_closure(matrix: list) -> list:
    """
    This function computes the symmetric closure of a given relation matrix.
    If an element (i, j) exists, it also adds (j, i).

    :param matrix: list of lists representing the relation matrix
    :return matrix: with symmetric closure

    >>> symmetric_closure([[0,1,0],[0,0,1],[0,0,0]])
    [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        """
    matrix = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                matrix[j][i] = 1
    return matrix


def transitive_closure(matrix: list) -> list:
    """
    This function computes the transitive closure of a matrix.
    It is using Uorshala algorithm.
    The alghorythm become slower with larger matrix size.

    :param matrix: list of lists representing the relation matrix
    :return matrix: with transitive closure

    >>> transitive_closure([[0,1,0],[0,0,1],[0,0,0]])
    [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    >>> transitive_closure([[1,1,0],[0,1,1],[0,0,1]])
    [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
    >>> transitive_closure([[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]])
    [[0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
    """

    matrix = deepcopy(matrix)
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
    return matrix

def check_tranz(matrix:list[list[int]]) -> bool:
    """
    Checks if a relation matrix is transitive.

    :param matrix: list of lists representing the relation matrix
    :return: True if transitive, False otherwise
    """
    n = len(matrix)
    matrix_2 = deepcopy(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix_2[i][j] = matrix_2[i][j] or (matrix_2[i][k] and matrix_2[k][j])
    return matrix == matrix_2

def relation_equl(matrix: list) -> list:
    """
    This function checks if a relation is an equivalence relation
    (reflexive, symmetric, and transitive).
    If yes, it returns the list of equivalence classes.
    If not, returns an empty list.

    :param matrix: list of lists representing the relation matrix
    :return: list of equivalence classes or an empty list

    >>> relation_equl([[1,1,0],[1,1,0],[0,0,1]])
    [[0, 1], [2]]
    """
    n = len(matrix)
    if matrix != reflexive_closure(matrix):
        print('Відношення не є рефлексивним')
        return []
    if matrix != symmetric_closure(matrix):
        print('Відношення не є симетричним')
        return []
    if not check_tranz(matrix):
        print('Відношення не є транзитивним')
        return []

    c = []
    for i in range(n):
        res = []
        for j in range(n):
            if matrix[i][j] == 1:
                res.append(j)
        c.append(res)
    res = []
    for i in c:
        if i not in res:
            res.append(i)
    return res


def matrix_by_num(num: int, n: int) -> list:
    """
    This function converts a number into an n×n matrix using it binary code.

    :param num: integer representing a binary relation
    :param n: matrix size
    :return: list of lists

    >>> matrix_by_num(4, 4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
    >>> matrix_by_num(0, 4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> matrix_by_num(511, 3)
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    """
    bin_num = bin(num)[2:].zfill(n * n)
    matrix = []
    for i in range(n):
        row = [int(x) for x in bin_num[i * n:(i + 1) * n]]
        matrix.append(row)
    return matrix


def count_transitive_relations(n: int) -> int:
    """
    This function counts how many transitive relations exist on a set with n elements.

    :param n: number of elements in the set
    :return: number of transitive relations
    >>> count_transitive_relations(3)
    171
    >>> count_transitive_relations(4)
    3994
    """
    count = 0
    for num in range(2 ** (n * n)):
        matrix = matrix_by_num(num, n)
        if check_tranz(matrix):
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
