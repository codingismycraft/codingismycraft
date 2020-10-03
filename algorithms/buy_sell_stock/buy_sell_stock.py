def left_side_max_deltas(prices):
    """Returns a list whose each element has the max delta from left side.

    :param list prices: The list of prices.

    :return: The list with the max delta from left.
    :rtype: list.
    """
    deltas = [0] * len(prices)
    largest_so_far = None
    lower_so_far = None
    m = 0
    for index, value in enumerate(prices):
        if largest_so_far is None or largest_so_far < value:
            largest_so_far = value

        if lower_so_far is None or lower_so_far > value:
            lower_so_far = value
            largest_so_far = 0

        m = max(m, largest_so_far - lower_so_far)
        deltas[index] = m

    return deltas


def right_side_max_deltas(prices):
    """Returns a list whose each element has the max delta from right side.

    :param list prices: The list of prices.

    :return: The list with the max delta from right.
    :rtype: list.
    """
    deltas = [0] * len(prices)
    index = len(prices) - 1

    largest_so_far = None
    lower_so_far = None
    m = 0

    while index >= 0:
        value = prices[index]

        if largest_so_far is None or largest_so_far < value:
            largest_so_far = value
            lower_so_far = value

        if lower_so_far is None or lower_so_far > value:
            lower_so_far = value

        m = max(m, largest_so_far - lower_so_far)
        deltas[index] = m

        index -= 1

    return deltas


def get_max_profit_(prices):
    m = 0
    index = 0
    left = left_side_max_deltas(prices)
    right = right_side_max_deltas(prices)
    while index < len(prices):
        m = max(m, left[index] + right[index])
        index += 1
    return m

def get_max_profit(prices):
    """Solves the problem in one function."""
    left = []
    min_price = None
    max_profit = 0

    for p in prices:
        if min_price is None or min_price > p:
            min_price = p
        if p - min_price > max_profit:
            max_profit = p - min_price
        left.append(max_profit)

    right = []
    max_price = None
    max_profit = 0

    for p in prices[::-1]:
        if max_price is None or max_price < p:
            max_price = p
        if max_price - p > max_profit:
            max_profit = max_price - p
        right.insert(0, max_profit)

    max_profit = 0

    for index in range(len(prices)):
        profit = left[index] + right[index]
        if profit > max_profit:
            max_profit = profit

    return max_profit
