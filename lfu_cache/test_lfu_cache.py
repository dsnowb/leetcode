from pytest import raises
from lfu_cache import Node, DLL, LFUCache


def test_length():
    """
    Validate length magic.
    """
    dll = DLL()
    assert len(dll) == dll.length


def test_dll_instance():
    """
    Validate initial instance properties.
    """
    dll = DLL()
    assert dll.head is None
    assert dll.tail is None
    assert len(dll) == 0


def test_dll_single_insert(empty_dll):
    """
    Validate single insertion.
    """
    empty_dll.insert(1)

    # Head and tail are the same Node
    assert empty_dll.head is empty_dll.tail
    assert type(empty_dll.head) is Node

    # Length has incremented
    assert len(empty_dll) == 1

    # Value is stored
    assert empty_dll.head.val == 1

    # A single node empty_dll has no next or previous nodes
    assert empty_dll.head._prev is None
    assert empty_dll.head._next is None


def test_dll_simple_insert(empty_dll):
    """
    Validate simple series of insertions.
    """
    for i in range(10):
        empty_dll.insert(i)

    # Length incremented each iteration
    assert len(empty_dll) == 10

    # Head stores last inserted value, and has no previous node
    node = empty_dll.head
    assert node.val == 9
    assert node._prev is None

    # Traverse DLL
    for i in range(8, 0, -1):
        node = node._next

        # Node values retain insertion order
        assert node.val == i

        # Previous and next are correctly ordered
        assert node._prev.val == i + 1
        assert node._next.val == i - 1

    # Tail stores first inserted value, and has no next node
    node = node._next
    assert node is empty_dll.tail
    assert node.val == 0
    assert node._next is None


def test_dll_single_append(empty_dll):
    """
    Validate single append.
    """
    empty_dll.append(1)

    # Head and tail are the same Node
    assert empty_dll.head is empty_dll.tail
    assert type(empty_dll.head) is Node

    # Length has incremented
    assert len(empty_dll) == 1

    # Value is stored
    assert empty_dll.head.val == 1

    # A single node empty_dll has no next or previous nodes
    assert empty_dll.head._prev is None
    assert empty_dll.head._next is None


def test_dll_simple_append(empty_dll):
    """
    Validate simple series of appends.
    """
    for i in range(10):
        empty_dll.append(i)

    # Length incremented each iteration
    assert len(empty_dll) == 10

    # Head stores first inserted value, and has no previous node
    node = empty_dll.head
    assert node.val == 0
    assert node._prev is None

    # Traverse DLL
    for i in range(1, 9):
        node = node._next

        # Node values retain insertion order
        assert node.val == i

        # Previous and next are correctly ordered
        assert node._prev.val == i - 1
        assert node._next.val == i + 1

    # Tail stores last inserted value, and has no next node
    node = node._next
    assert node is empty_dll.tail
    assert node.val == 9
    assert node._next is None


def test_dll_single_remove_head(single_dll):
    """
    Validate single remove head.
    """
    single_dll.remove(single_dll.head)

    # Head and tail are None
    assert single_dll.head is None
    assert single_dll.tail is None

    # Length has been decremented
    assert len(single_dll) == 0


def test_dll_single_remove_tail(single_dll):
    """
    Validate single remove tail.
    """
    single_dll.remove(single_dll.tail)

    # Head and tail are None
    assert single_dll.head is None
    assert single_dll.tail is None

    # Length has been decremented
    assert len(single_dll) == 0


def test_dll_simple_remove_head(simple_dll):
    """
    Validate remove head from multi-node DLL.
    """
    # Initial state
    head_next = simple_dll.head._next
    tail = simple_dll.tail

    simple_dll.remove(simple_dll.head)

    # Head is updated, tail is unchanged
    assert simple_dll.head is head_next
    assert simple_dll.head._prev is None
    assert simple_dll.tail is tail


def test_dll_simple_remove_tail(simple_dll):
    """
    Validate remove tail from multi-node DLL.
    """
    # Initial state
    tail_prev = simple_dll.tail._prev
    head = simple_dll.head

    simple_dll.remove(simple_dll.tail)

    # Tail is updated, head is unchanged
    assert simple_dll.tail is tail_prev
    assert simple_dll.tail._next is None
    assert simple_dll.head is head


def test_dll_middle_remove(simple_dll):
    """
    Validate removal of middle node.
    """
    # Initial state
    initial_len = len(simple_dll)

    # Select 2nd node
    node = simple_dll.head._next

    simple_dll.remove(node)

    # Head's next is now 3rd node and 3rd node's previous is now head
    assert simple_dll.head._next is node._next
    assert node._next._prev is simple_dll.head

    # Length has been decremented
    assert len(simple_dll) == initial_len - 1


def test_lfu_instance():
    """
    LFU Instantiates with expected values.
    """
    lfu = LFUCache(1)
    assert lfu.capacity == 1
    assert lfu.size == 0
    assert lfu.items == {}
    assert isinstance(lfu.lfu, DLL)
    assert len(lfu.lfu) == 0


def test_empty_lfu_single_put(empty_lfu):
    """
    Validate single put into empty LFU.
    """
    empty_lfu.put(1, 10)

    # Size has incremented.
    assert empty_lfu.size == 1

    # Value is stored.
    assert empty_lfu.items[1]['value'] == 10

    # Should be stored in least-frequently used node, which is head
    assert empty_lfu.items[1]['lfu'] is empty_lfu.lfu.head

    # Should be the most recently used node for that LFU position
    assert empty_lfu.items[1]['lru'] is empty_lfu.lfu.head.val[1].head

    # LFU DLL should contain one node
    assert len(empty_lfu.lfu) == 1

    # That node should contain a DLL with one node of its own, and a freq. of 1
    assert len(empty_lfu.lfu.head.val[1]) == 1
    assert empty_lfu.lfu.head.val[0] == 1


def test_simple_lfu_put(empty_multi_lfu):
    """
    Validate multiple puts.
    """
    for i in range(10):
        empty_multi_lfu.put(i, i*10)

    # Correctly count items
    assert len(empty_multi_lfu) == 10

    # All items have a frequency of 1
    assert len(empty_multi_lfu.lfu) == 1


def test_single_get(small_lfu):
    """
    Single get test
    """
    # Value is correctly retrieved
    assert small_lfu.get(1) == 10

    # Size of LFU unchanged
    assert len(small_lfu) == 10

    # Len of frequency DLL increased
    assert len(small_lfu.lfu) == 2

    # Frequency of new LFU node is correct
    assert small_lfu.lfu.head._next.val[0] == 2


def test_simple_lfu_two_get(small_lfu):
    """
    Test double get of smale key results in correct structure.
    """
    for i in range(2):
        assert small_lfu.get(1) == 10

    # Validate structure
    assert len(small_lfu.lfu) == 2
    assert small_lfu.lfu.head.val[0] == 1
    assert small_lfu.lfu.head._next.val[0] == 3

    assert len(small_lfu.lfu.head.val[1]) == 9
    assert len(small_lfu.lfu.head._next.val[1]) == 1


def test_simple_lfu_multi_get(small_lfu):
    """
    Test multiple gets result in correct structure.
    """

    # Validate value retrieval
    assert small_lfu.get(2) == 20
    for i in range(10):
        assert small_lfu.get(1) == 10
    assert small_lfu.get(2) == 20
    assert small_lfu.get(3) == 30

    # Validate structure
    assert len(small_lfu.lfu) == 4
    assert small_lfu.lfu.head.val[0] == 1
    assert small_lfu.lfu.head._next.val[0] == 2
    assert small_lfu.lfu.head._next._next.val[0] == 3
    assert small_lfu.lfu.head._next._next._next.val[0] == 11


def test_single_lfu_single_evict(single_lfu):
    """
    Test evicting from single element LFU.
    """
    single_lfu.evict()

    # Size decrements
    assert single_lfu.size == 0

    # Key not in cache
    with raises(KeyError):
        assert single_lfu.items[1]

    # No nodes should exist in LFU
    assert len(single_lfu.lfu) == 0


def test_simple_lfu_put_auto_evict(single_lfu):
    """
    Test putting into a full LFU correctly evicts.
    """
    single_lfu.put(2, 20)

    # Length remains at max
    assert len(single_lfu) == 1

    # Old key/value has been replaced with new
    with raises(KeyError):
        assert single_lfu.items[1]

    assert single_lfu.items[2]['value'] == 20


def test_lfu_lru_tie_breaker(small_lfu):
    """
    Test LRU tie breaking for eviction
    """

    # Set up tie for LFU
    small_lfu.get(0)
    small_lfu.get(1)
    for i in range(2, 10):
        for j in range(10):
            small_lfu.get(i)

    small_lfu.put(10, 100)

    # LRU is evicted
    assert len(small_lfu.lfu) == 3
    assert len(small_lfu.lfu.head._next.val[1]) == 1
    assert small_lfu.lfu.head._next.val[1].head.val == 1


def test_lfu_key_in_lfu(small_lfu):
    """
    Test updating an existing key, value pair
    """
    small_lfu.put(1, 'a')

    assert small_lfu.get(1) == 'a'
