"""See description of the problem in leet code.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3964/
"""

import heapq


def get_index_to_delete(array, low, hi, char_to_add):
    min_index = low
    min_value = array[low]

    for i in range(low, hi):
        if array[i] == char_to_add:
            continue
        if array[i] < min_value:
            min_index = i
            min_value = array[i]

    return min_index


def solve_it(s, k):
    heap = list(s)
    heapq.heapify(heap)
    response = list(str(s))

    for index in range(0, k):
        char_to_add = heapq.heappop(heap)
        while response[index] != char_to_add:
            i = get_index_to_delete(response, index, k, char_to_add)
            char_to_move = response[i]
            del response[i]
            response += [char_to_move]

    return ''.join(response)

