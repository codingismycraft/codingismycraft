"""Tests the efficient solution."""

import unittest

import efficient_solution

# Aliases.
RecordStatus = efficient_solution.RecordStatus
count_sequences = efficient_solution.count_sequences


class EfficientSolutionTest(unittest.TestCase):
    """Tests the efficient solution."""

    def test_count(self):
        """Tests the student record count."""

        testing_data = {
            1: 3,
            2: 8,
            3: 19,
            4: 43,
            5: 94,
            6: 200,
            7: 418,
            8: 861,
            9: 1753,
            10: 3536,
            11: 7077,
            12: 14071,
            13: 27820,
            14: 54736,
            15: 107236,
            16: 209305,
            17: 407167
        }

        for n, expected_count in testing_data.items():
            self.assertEqual(expected_count, RecordStatus.count(n))

    def test_count_sequences(self):
        """Tests the count_sequences method."""

        testing_data = {
            1: 3,
            2: 8,
            3: 19,
            4: 43,
            5: 94,
            6: 200,
            7: 418,
            8: 861,
            9: 1753,
            10: 3536,
            11: 7077,
            12: 14071,
            13: 27820,
            14: 54736,
            15: 107236,
            16: 209305,
            17: 407167
        }

        for n, expected_count in testing_data.items():
            self.assertEqual(expected_count, count_sequences(n))


if __name__ == '__main__':
    unittest.main()
