class Node:
    """
    Trie node
    """
    def __init__(self, val=None):
        self.children = {}
        self.val = val


class Trie:
    """
    Trie tree data structure.
    """
    def __init__(self, word_list=[]):
        """
        Initialize trie.
        """
        self.root = Node()

        for word in word_list:
            self.insert(word)

    def insert(self, word, val=None):
        """
        Insert word into trie.
        """
        cur = self.root
        for i in range(len(word)):
            fragment = word[:i + 1]
            if fragment not in cur.children:
                cur.children[fragment] = Node()
            cur = cur.children[fragment]

    def traverse(self, func):
        pass
