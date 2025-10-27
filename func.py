from copy import deepcopy
import csv


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


def write_relation(matrix: list, filename: str) -> None:
    """
    This function writes a matrix to a CSV file where each row is saved as a single string.
    If the file does not exist, it will be created automatically.
    If the file already exists, its previous content will be completely overwritten.

    :param matrix: list of lists representing the relation matrix
    :param filename: name of the CSV file to write to
    :return: None
    """
    with open(filename, 'w') as file:
        csv_writer = csv.writer(file)
        for row in matrix:
            csv_writer.writerow(["".join(str(el) for el in row)])


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
    result = matrix.copy()
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i][j] = result[i][j] or (result[i][k] and result[k][j])
    return result


