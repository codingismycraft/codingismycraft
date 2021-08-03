"""Test the prim module."""

import unittest

import prim


class TestPrim(unittest.TestCase):
    """Tests the prim function."""

    def test_prim_example_1(self):
        """Tests the prim function using prim-example_1.png."""
        data = {
            '1': [('2', 6), ('3', 1)],
            '2': [('1', 6), ('3', 5), ('4', 7), ('6', 3)],
            '3': [('1', 1), ('2', 5), ('4', 6)],
            '4': [('2', 7), ('3', 6), ('5', 8), ('6', 2)],
            '5': [('4', 8)],
            '6': [('2', 3), ('4', 2)],
        }
        expected_path = [
            ['1', '3'], ['3', '2'], ['2', '6'], ['6', '4'], ['4', '5']
        ]
        expected_weight = 19
        path, w = prim.prim(data)
        self.assertListEqual(path, expected_path)
        self.assertEqual(w, expected_weight)

    def test_prim_example_2(self):
        """Tests the prim function using prim-example_1.png."""
        data = {
            '1': [('6', 10), ('2', 28)],
            '2': [('1', 28), ('7', 14), ('3', 16)],
            '3': [('2', 16), ('4', 12)],
            '4': [('3', 12), ('7', 18), ('5', 22)],
            '5': [('4', 22), ('7', 24), ('6', 25)],
            '6': [('1', 10), ('5', 25)],
            '7': [('5', 24), ('4', 18), ('2', 14)],
        }
        expected_path = [
            ['1', '6'], ['6', '5'], ['5', '4'], ['4', '3'],
            ['3', '2'], ['2', '7']
        ]
        expected_weight = 99
        path, w = prim.prim(data)
        self.assertListEqual(path, expected_path)
        self.assertEqual(w, expected_weight)


if __name__ == '__main__':
    unittest.main()
