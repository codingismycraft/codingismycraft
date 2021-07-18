import trie
import datetime

# Aliases
Trie = trie.Trie


def make_root():
    words = []
    with open("/vagrant/algorithms/trie/dictionary") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.append(word)
    root = Trie()
    for word in words:
        root.add(word)
    return root


def make_suggestion(prefix):
    print(root.get_suggestions(prefix))


if __name__ == '__main__':
    root = make_root()

    while True:
        prefix = input("Enter prefix: ")
        make_suggestion(prefix)