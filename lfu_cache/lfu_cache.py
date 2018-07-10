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

    def __len__(self):
        """
        Return size
        """
        return self.size

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Attempt to return value at key
        try:
            item = self.items[key]
            self.update(item)
            return item['value']

        except KeyError:
            return -1

    def update(self, item):
        """
        Moves item forward in LFU DLL, to head (MRU) of new LRU DLL.
        """
        # Remove LRU node from current LFU node
        item['lfu'].val[1].remove(item['lru'])

        # If next LFU does not exist or is not +1 freq, create a new node
        # with +1 freq and insert as next LFU node.
        if (not item['lfu']._next or
                item['lfu']._next.val[0] != item['lfu'].val[0] + 1):

                    # Create new node
                    newLFU = Node((item['lfu'].val[0] + 1, DLL()))

                    # Update tail if necessary
                    if not item['lfu']._next:
                        self.lfu.tail = newLFU

                    # Update next
                    newLFU._next = item['lfu']._next
                    try:
                        item['lfu']._next._prev = newLFU
                    except AttributeError:
                        pass

                    # Update previous
                    newLFU._prev = item['lfu']
                    item['lfu']._next = newLFU

                    self.lfu.length += 1

        # Remove LFU node if contains no LRU nodes
        if len(item['lfu'].val[1]) == 0:
            self.lfu.remove(item['lfu'])

        # Update LFU to next
        item['lfu'] = item['lfu']._next

        # Insert LRU node into new LRU DLL
        item['lfu'].val[1].insert(item['lru'].val)
        item['lru'] = item['lfu'].val[1].head

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        # If at capacity, evict.
        if self.size == self.capacity:
            self.evict()

        # Insert a new key-value pair.

        # In addition to key/value, stored values include:
        # LFU/LRU nodes so that when accessed, LFU/LRU can be updated O(1)
        # The LRU DLL for a a given frequency is paired with an actual usage
        # frequency because usage frequencies may be non-sequential

        if key not in self.items:

            # Insert into LFU node with frequency 1, at most recently used
            # position (head) of corresponding LRU DLL
            if not self.lfu.head or self.lfu.head.val[0] != 1:
                self.lfu.insert((1, DLL()))
            self.lfu.head.val[1].insert(key)

            # Create entry for key/value lookup and LRU/LFU node access
            self.items[key] = {
                'value': value,
                'lfu': self.lfu.head,
                'lru': self.lfu.head.val[1].head,
            }

        # Update an existing key-value pair

        # In addition to updating the value at key, updates include:
        # LFU - Move to +1 frequency LFU. Create that LFU node if necessary.
        # LRU - Remove from current LRU DLL, insert at most recent position
        # for new frequency.

        else:
            item = self.items[key]
            item['value'] = value
            self.update(item)

        # Increment size
        self.size += 1

    def evict(self):

        # From the least frequently used DLL (the head of the LFU DLL)
        # select the least recently used node (the tail of the LRU DLL)
        node = self.lfu.head.val[1].tail

        # Remove that node from it's LRU DLL
        self.lfu.head.val[1].remove(node)

        # If the LRU DLL is now empty, remove its parent LFU node
        if len(self.lfu.head.val[1]) == 0:
            self.lfu.remove(self.lfu.head)

        # Remove key/value pair from items
        del self.items[node.val]

        # Decrement size of LFU
        self.size -= 1
