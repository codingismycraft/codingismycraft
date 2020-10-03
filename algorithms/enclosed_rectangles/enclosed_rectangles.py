"""Solves the how many rects are contained in a grid problem.

Assumes a perfect grid containing all points.  A sparse grid is a more
specialized case that can be solved similarly by removing the missing
points.
"""
import itertools


def count_rectangles(n):
    """Counts rectangles in constant time O(0).

    :param int n: The number of points in each dimension (x, y). Applies to
    a square; a rectangle will be a variation of this logic.

    :return: The number of contained sub-rectangles.
    :rtype: int
    """
    n = n
    m = n * n
    pairs = (m - 1) * m / 2
    lines = (n - 1) * n * n
    net_pairs = (pairs - lines) / 2
    return net_pairs


def count_rectangles3(n):
    """Counts rectangles in constant time O(0).

    :param int n: The number of points in each dimension (x, y). Applies to
    a square; a rectangle will be a variation of this logic.

    :return: The number of contained sub-rectangles.
    :rtype: int
    """

    return pow(n * (n - 1) / 2, 2)


def count_rectangles2(n):
    """" Returns number of enclosed rectangle."""
    if n <= 1:
        return 0
    dp = [0 for _ in range(n + 1)]
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + pow(i - 1, 3)

    return dp[-1]


def print_rectangles(points):
    """Prints all rects in O(N^2).

    Assumes that points represent a square; solving for a rectangle will be
    a special case of the same idea.

    :param list points: A two dimensional list representing the points of
    a square.
    """
    points = list(itertools.chain(*points))
    point_pairs = list(itertools.combinations(points, 2))
    # Remove same x
    point_pairs = [p for p in point_pairs if p[0][0] != p[1][0]]
    # Remove same y
    point_pairs = [p for p in point_pairs if p[0][1] != p[1][1]]
    # Remove the reversed diagonals.
    point_pairs = [p for p in point_pairs if p[0][1] < p[1][1]]

    for (x1, y1), (x2, y2) in point_pairs:
        print((x1, y1), (x2, y1), (x1, y2), (x2, y2))
    print("Total: {}".format(len(point_pairs)))


if __name__ == '__main__':

    for i in range(2, 10):
        c = count_rectangles(i)
        c1 = count_rectangles2(i)
        c3 = count_rectangles3(i)
        assert c1 == c == c3

    i = 11826
    c = count_rectangles(i)
    print("Matrix: {} X {} has {:6} rects".format(i, i, int(c)))

    # Solving with Points
    points = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
    ]
    print_rectangles(points)

    points = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(1, 0), (1, 1), (1, 2), (1, 3)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
        [(3, 0), (3, 1), (3, 2), (3, 3)],
    ]
    print_rectangles(points)

    points = [
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],
    ]
    print_rectangles(points)
