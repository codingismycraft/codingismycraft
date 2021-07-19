"""Simple autocompletion utility using Trie."""

import trie

# Aliases.
Trie = trie.Trie
_WORDS_FILE_NAME = "/vagrant/algorithms/trie/dictionary"


def make_root():
    """Makes the root Trie.

    Loads the root trie with all the words contained in the dictionary.

    :return: The root Trie node.
    :rtype: Trie.
    """
    words = []
    with open(_WORDS_FILE_NAME) as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.append(word)
    root = Trie()
    for word in words:
        root.add(word)
    return root


def make_suggestion(prefix, root):
    """Finds the possible suggestions for the passed in prefix.

    :param str prefix: The prefix lookup.
    :param Trie root: The root trie to use.

    :return: The suggestions for the passed in prefix.
    :rtype: list [str]
    """
    prefix = prefix.strip().lower()
    print(root.get_suggestions(prefix))


def main():
    """Receives input from used and displays the matches."""
    root = make_root()
    while True:
        prefix = input("Enter prefix: ")
        make_suggestion(prefix, root)


if __name__ == '__main__':
    main()
