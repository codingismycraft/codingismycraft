""""""

class Trie:
    def __init__(self):
        self.children={}
        self.eof=False

    def add_word(self,word):
        if not word:
            return
        first_letter=word[0]
        remainder=word[1:]
        if first_letter not in self.children:
            self.children[first_letter]=Trie()
        if not remainder:
            self.children[first_letter].eof=True
        else:
            self.children[first_letter].add_word(remainder)

    def contains_word(self,word):
        if not word:
            return False
        first_letter = word[0]
        remainder = word[1:]
        if first_letter not in self.children:
            return False
        if not remainder:
            return self.children[first_letter].eof
        else:
            return self.children[first_letter].contains_word(remainder)



root=Trie()
root.add_word("hello")
root.add_word("hey all")
def print_trie(obj):
    for v, c in obj.children.items():
        print(v)
        #print_trie(c)
print_trie(root)
print(root.contains_word("hello"))