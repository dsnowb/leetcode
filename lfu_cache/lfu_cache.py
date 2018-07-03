class Node:
    """
    Double linked list node.

    """
    def __init__(self, val, _next=None, _prev=None):
        self.val = val
        self._next = _next
        self._prev = _prev


class DLL:
    """
    Double linked list.

    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert(self, val):
        """
        Insert node at head of DLL.
        """
        if not self.length:
            self.head = self.tail = Node(val)
        else:
            node = Node(val, self.head)
            self.head._prev = node
            self.head = node

        self.length += 1

    def append(self, val):
        """
        Insert node at tail of DLL.
        """
        if not self.length:
            self.head = self.tail = Node(val)
        else:
            self.tail._next = Node(val, _prev=self.tail)
            self.tail = self.tail._next

        self.length += 1

    def remove(self, node):
        """
        Remove node at arbitrary location from DLL.
        """
        if not self.length:
            return
        if self.length == 1:
            self.head = self.tail = None
        else:
            if self.head is node:
                self.head = self.head._next
            if self.tail is node:
                self.tail = self.tail._prev

            try:
                node._prev._next = node._next
            except AttributeError:
                pass

            try:
                node._next._prev = node._prev
            except AttributeError:
                pass

        self.length -= 1


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.items = {}
        self.lfu = DLL()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            item = self.items[key]
            self.update(item)
            return item['value']

        except KeyError:
            return -1

    def update(self, node):
        pass

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        # Insert a new key-value pair.
        if key not in self.items:
            try:
                self.lfu.head.val.insert(key)
            except AttributeError:
                self.lfu.head = Node(DLL())
                self.lfu.head.val.insert(key)

            self.items[key] = {
                'value': value,
                'lfu': self.lfu.head,
                'lru': self.lfu.head.val.head,
            }

            if self.size < self.capacity:
                self.size += 1

        # Update an existing key-value pair
        else:
            item = self.items[key]

            # Remove LRU node from current LFU node
            item['lfu'].val.remove(item['lru'])

            # Attempt to update LFU node
            try:
                item['lfu'] = item['lfu']._next

            # If at front of LFU, create new LFU node
            except AttributeError:
                self.items[key]['lfu']._next = \
                                self.items[key]['lfu'].append(DLL())

                # Update LFU node after node creation
                item['lfu'] = item['lfu']._next

            # Insert new LRU node at new LFU node
            item['lfu'].val.insert(Node(item['lru'].val))

            # Update LRU node after insertion
            item['lru'] = item['lfu'].val.head

        if self.size == self.capacity:
            self.evict()

    def evict(self):
        node = self.lfu.head.val.tail
        self.lfu.head.val.remove(node)
        del self.items[node.val]
