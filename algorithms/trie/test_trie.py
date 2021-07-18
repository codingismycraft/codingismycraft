"""Test the trie module."""

import unittest
import trie

# Aliases
Trie = trie.Trie

_WORDS = [
    "lanyards",
    "lanzhou",
    "laocoon",
    "rebroadcasting",
    "rebroadcasts",
    "rebuff",
    "sculley",
    "sculling",
    "scullion",
    "cannonade",
    "cannonaded",
    "cannonades",
]


class TestTrie(unittest.TestCase):
    """Tests the trie class."""

    def test_insertion(self):
        """Tests inserting to trie instance."""
        root = Trie()
        for word in _WORDS:
            root.add(word)

        for word in _WORDS:
            self.assertTrue(root.exists(word))
            self.assertFalse(root.exists(word + "JUNK"))

        self.assertFalse("")

    def test_set_set_end_of_word(self):
        root = Trie()
        root.add("l")
        self.assertTrue(root.exists("l"))

    def test_get_all_words(self):
        root = Trie()
        for word in _WORDS:
            root.add(word)
        retrieved = root.get_all_words()

        self.assertListEqual(sorted(_WORDS), sorted(retrieved))

    def test_get_suggestions(self):
        root = Trie()
        for word in _WORDS:
            root.add(word)

        retrieved = root.get_suggestions("lan")
        expected = [
            "lanyards",
            "lanzhou"
        ]
        self.assertListEqual(sorted(expected), sorted(retrieved))


if __name__ == '__main__':
    unittest.main()
