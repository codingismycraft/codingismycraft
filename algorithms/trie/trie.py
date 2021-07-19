"""Exposes the Trie algorithm."""


class Trie:
    """A Trie node holding its descendants in a dictionary.

    :ivar dict _children: Dict from a single character to a Trie node.
    :ivar bool _end_of_word: True if the Trie instance denotes a word end.
    """

    _children = None
    _end_of_word = None

    def __init__(self):
        """Initializer."""
        self._children = {}
        self._end_of_word = False

    def __repr__(self):
        return f'Trie: children: {self._children.keys()} ' \
               f'eow: {self._end_of_word}'

    def set_end_of_word(self):
        """Marks the instance as ending of word."""
        self._end_of_word = True

    def is_end_of_word(self):
        """Checks is the instance is end of a word.

        :return: True if the instance is end of a word.
        :rtype: bool
        """
        return self._end_of_word

    def add(self, word):
        """Adds a word.

        :param str word: The word to add.
        """
        first_letter, remainder = word[0], word[1:]
        if first_letter not in self._children:
            self._children[first_letter] = Trie()

        if not remainder:
            self._children[first_letter].set_end_of_word()
        else:
            self._children[first_letter].add(remainder)

    def exists(self, word):
        """Checks if the passed in word existing in trie.

        :param str word: The word to add.

        :return: True if the passed in word existing in trie.
        :rtype: bool
        """
        first_letter, remainder = word[0], word[1:]
        if first_letter not in self._children:
            return False
        else:
            if not remainder:
                return self._children[first_letter].is_end_of_word()

            return self._children[first_letter].exists(remainder)

    def get_all_words(self, prefix=''):
        """Gets all the dictionary contained in the Trie instance.

        :param str prefix: The prefix to add in each found word.

        :return: A list of all the available dictionary for the given
            Trie (node).
        :rtype: list [str]
        """
        words = []
        for first_char, child in self._children.items():

            if child.is_end_of_word():
                new_word = prefix + first_char
                words.append(new_word)

            words.extend(child.get_all_words(prefix + first_char))
        return words

    def search(self, prefix):
        """Finds the Trie node pointing to the last character in prefix.

        :return: The Trie node pointing to the last character in prefix.
        :rtype: Trie
        """
        if not prefix:
            return None
        first_letter, remainder = prefix[0], prefix[1:]
        if first_letter not in self._children:
            return None
        if not remainder:
            return self._children[first_letter]
        else:
            return self._children[first_letter].search(remainder)

    def get_suggestions(self, prefix):
        """Gets the possible suggestions for the passed in prefix.

        :param str prefix: The prefix to look up.

        :return: A list of matching strings for the passed in prefix.
        :rtype: list [str]
        """
        parent = self.search(prefix)
        if not parent:
            return []

        suggestions = []
        for word in parent.get_all_words():
            suggestions.append(prefix + word)

        return suggestions
