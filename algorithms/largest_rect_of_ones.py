import copy

matrix = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

expected = 2


def find_max_square(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    matrix = copy.deepcopy(matrix)
    max_value = 0
    for col in range(1, cols):
        for row in range(1, rows):
            if matrix[col][row]:
                diagonal = matrix[col - 1][row - 1]
                above = matrix[col - 1][row]
                left = matrix[col][row - 1]
                matrix[col][row] += min(diagonal, above, left)
                max_value = max(max_value, matrix[col][row])
    return max_value


def find_max_square_1(matrix):
    """A slightly different implementation."""
    max_square = 1
    matrix = copy.deepcopy(matrix)
    for i in range(1, len(matrix)):
        row = matrix[i]
        for j in range(1, len(row)):
            if row[j] != 0:
                above = matrix[i-1][j]
                left = matrix[i][j-1]
                diagonal = matrix[i-1][j-1]
                row[j] = min(above, left, diagonal) + 1
                if row[j] > max_square:
                    max_square = row[j]
    return max_square



print(find_max_square(matrix))
