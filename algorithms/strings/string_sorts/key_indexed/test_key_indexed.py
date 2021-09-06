"""Tests the key_indexed module."""

import datetime
import unittest

import key_indexed
import utils
import qsort

# Alias.
key_indexed_sort = key_indexed.key_indexed_sort
qsort = qsort.qsort


class Student:

    def __init__(self, name, sector):
        self.name = name
        self.sector = sector

    def __lt__(self, other):
        return self.sector < other.sector

    def __eq__(self, other):
        return self.sector == other.sector

    def __ge__(self, other):
        return self.sector >= other.sector


class TestKeyIndexed(unittest.TestCase):
    """Test the key_indexed module."""

    def vefiry_solution(self, retrieved):
        current_sector = retrieved[0].sector
        for s in retrieved:
            self.assertTrue(s.sector >= current_sector)
            current_sector = s.sector

    def test_key_indexed_sort(self):
        """Tests the sort function."""
        data = [
            Student('Christian Long', 2),
            Student('Brittney Ayala', 3),
            Student('Eric Macias', 2),
            Student('Lindsey Harvey', 3),
            Student('Sandra Sanders', 2),
            Student('Mr. Timothy Young', 2),
            Student('Chloe Huang', 1),
            Student('Tonya Jones', 1),
            Student('Erica Archer', 3),
            Student('David Martinez', 3)
        ]

        retrieved = key_indexed_sort(data, 1, 3)
        expected = sorted(data, key=lambda d: d.sector)
        self.assertListEqual(retrieved, expected)
        self.vefiry_solution(retrieved)

    def test_performance(self):
        """Compares the performance against a regular sort."""
        students = [Student(name, sector) for name, sector in utils.read_data()]

        t1 = datetime.datetime.now()
        expected = students[:]
        qsort(expected)
        t2 = datetime.datetime.now()
        regular_sort_duration = (t2 - t1).total_seconds()
        print(f'Regular sort duration: {regular_sort_duration} seconds')

        t1 = datetime.datetime.now()
        retrieved = key_indexed_sort(students, 1, 5)
        t2 = datetime.datetime.now()
        key_indexed_sort_duration = (t2 - t1).total_seconds()

        self.assertListEqual(retrieved, expected)

        print(f'{len(retrieved)}, {len(expected)}')

        print(f'key indexed duration: {key_indexed_sort_duration} seconds')
        print(Student.counter)

        print(regular_sort_duration / key_indexed_sort_duration)


if __name__ == '__main__':
    unittest.main()
