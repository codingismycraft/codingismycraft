"""See description of the problem in leet code.

https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3964/
"""

import heapq


def solve_it(s, k):
    heap = list(s)
    heapq.heapify(heap)
    response = str(s)

    for index in range(0, k):
        print(response)
        char = heapq.heappop(heap)
        j = response.index(char, index)

        a = response[0:index]
        b = response[j:]
        c = response[index:j]
        d = ''.join(sorted(list(response[index:k -index])))
        e = response[k -index:j]


        response = response[0:index] + response[j:] + response[index:j]
    print(response)
    return response

