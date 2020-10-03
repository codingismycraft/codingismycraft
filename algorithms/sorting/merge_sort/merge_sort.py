"""Implements merge sort."""


def two_way_merge(arr, lo, cutoff, hi, temp):
    i1 = lo
    i2 = cutoff + 1
    j = lo

    while i1 <= cutoff and i2 <= hi:
        if arr[i1] < arr[i2]:
            temp[j] = arr[i1]
            i1 += 1
            j += 1
        elif arr[i1] > arr[i2]:
            temp[j] = arr[i2]
            i2 += 1
            j += 1
        else:
            temp[j] = arr[i1]
            i1 += 1
            j += 1

            temp[j] = arr[i2]
            i2 += 1
            j += 1

    while i1 <= cutoff:
        temp[j] = arr[i1]
        i1 += 1
        j += 1

    while i2 <= hi:
        temp[j] = arr[i2]
        i2 += 1
        j += 1

    for j in range(lo, hi + 1):
        arr[j] = temp[j]


def merge_sort(arr, low, hi, temp=None):
    if low == hi:
        return
    temp = temp or [None] * len(arr)
    middle = (hi + low) // 2
    merge_sort(arr, low, middle, temp)
    merge_sort(arr, middle + 1, hi, temp)
    two_way_merge(arr, low, middle, hi, temp)
