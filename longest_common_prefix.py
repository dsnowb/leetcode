class Node:
    def __init__(self, val=''):
        self.val = val
        self.children = {}
        self.isend = False


class Trie:
    def __init__(self, strs):
        self.root = Node()
        for s in strs:
            self.insert(s)

    def insert(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.isend = True


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        t = Trie(strs)

        prefix = ''
        cur = t.root
        while len(cur.children) == 1 and not cur.isend:
            prefix += cur.val
            cur = cur.children[list(cur.children.keys())[0]]

        return prefix + cur.val
