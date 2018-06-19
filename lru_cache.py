class Node:
    def __init__(self, val=None, _next=None, _prev=None):
        """
        Init.
        """
        self._next = _next
        self._prev = _prev
        self.val = val


class DLL:
    def __init__(self):
        """
        Init.
        """
        self.head = None
        self.tail = None

    def to_head(self, node):
        """
        Move node to head, otherwise maintaining order.
        """
        if self.head == node:
            return
        if node._prev:
            node._prev._next = node._next
            if self.tail == node:
                self.tail = node._prev
        if node._next:
            node._next._prev = node._prev
        node._prev = None
        node._next = self.head
        self.head._prev = node
        self.head = node

    def __str__(self):
        """
        String.
        """
        cur = self.head
        res = ''
        while cur:
            res += '({})'.format(cur.val)
            cur = cur._next
        return res

    def insert(self, val):
        """
        Insert val as node.
        """
        self.head = Node(val, self.head)

        if not self.tail:
            self.tail = self.head
            return

        self.head._next._prev = self.head

    def pop(self):
        """
        Replace tail with second to last.
        """
        if self.tail:
            if self.tail == self.head:
                self.tail = self.head = None
                return
            self.tail._prev._next = None
            self.tail = self.tail._prev


class LRUCache:
    """
    Implementation of LRU Caching.
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.recent = DLL()
        self.cache = {}
        self.size = 0
        self.capacity = capacity

    def get(self, key):
        """
        Retrieve key.
        """
        try:
            self.recent.to_head(self.cache[key][0])
        except KeyError:
            return -1

        return self.cache[key][1]

    def put(self, key, value):
        """
        Insert key and, if applicable, evict last used.
        """
        if key in self.cache:
            self.cache[key][1] = value
            self.recent.to_head(self.cache[key][0])
            return

        if self.size == self.capacity:
            del self.cache[self.recent.tail.val]
            self.recent.pop()
            self.size -= 1

        self.recent.insert(key)
        self.cache[key] = [self.recent.head, value]
        self.size += 1
