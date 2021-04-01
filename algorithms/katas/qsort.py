import unittest

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

def partition(array, start, end):
    pivot = array[end]
    index = start
    low = start

    while index <= end - 1:
        if array[index] < pivot:
            swap(array, index, low)
            low +=1
        index += 1

    if array[low] > pivot:
        swap(array, low, end)

    return low

def qsort(array, start, end):
    if start < end:
        i1 = partition(array, start, end)
        qsort(array, start, i1-1)
        qsort(array, i1+1, end)


class QSortTest(unittest.TestCase):
    def test_qsort(self):
        a = [1, 9, 7, 2, 12, 21, 0]
        qsort(a, 0, len(a) - 1)
        self.assertListEqual(sorted(a), a)


if __name__ == '__main__':
    unittest.main()





