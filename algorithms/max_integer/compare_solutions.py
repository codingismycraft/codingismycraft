"""Compares the performance of brutal vs efficient solutions."""

import datetime
import random

import brutal_solution_1 as brutal_solution
import solution

def make_integer(length):
    """Rerurns a random integer expressed as string.

    :param int length: The length of the string to return.

    :return: A random integer expressed as string.
    :rtype: str.
    """
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

if __name__ == '__main__':
    i = 0
    length = 30000
    flips = 1000000
    while True:
        num = make_integer(length)
        t1 = datetime.datetime.now()
        s1 = solution.minInteger(num, flips)
        t2 = datetime.datetime.now()
        print("sol",(t2-t1).total_seconds())
        t1 = datetime.datetime.now()
        s2 = brutal_solution.minInteger(num, flips)
        t2 = datetime.datetime.now()
        print("brut",(t2 - t1).total_seconds())
        if s1 != s2:
            print("here")
            print(num)
            print(s1)
            print(s2)
            break
        i += 1
        print(i)
