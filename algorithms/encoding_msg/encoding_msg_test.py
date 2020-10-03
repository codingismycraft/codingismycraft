"""Tests the encoding_msg module."""

import unittest

import encoding_msg

# Aliases.
count_matches = encoding_msg.count_matches


class EncodingMsg(unittest.TestCase):
    """Tests the encoding_msg module."""

    def test_encoding_msg(self):
        """Tests the count_matches function."""
        self.assertEqual(count_matches('10'), 1)
        self.assertEqual(count_matches('12'), 2)
        self.assertEqual(count_matches('123'), 3)
        self.assertEqual(count_matches('1213'), 5)
        self.assertEqual(count_matches('26113'), 6)


if __name__ == '__main__':
    unittest.main()
