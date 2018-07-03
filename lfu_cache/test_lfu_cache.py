from lfu_cache import Node, DLL


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


def test_single_insert(empty_dll):
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


def test_simple_insert(empty_dll):
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


def test_single_append(empty_dll):
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


def test_simple_append(empty_dll):
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


def test_single_remove_head(single_dll):
    """
    Validate single remove head.
    """
    single_dll.remove(single_dll.head)

    # Head and tail are None
    assert single_dll.head is None
    assert single_dll.tail is None

    # Length has been decremented
    assert len(single_dll) == 0


def test_single_remove_tail(single_dll):
    """
    Validate single remove tail.
    """
    single_dll.remove(single_dll.tail)

    # Head and tail are None
    assert single_dll.head is None
    assert single_dll.tail is None

    # Length has been decremented
    assert len(single_dll) == 0


def test_simple_remove_head(simple_dll):
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


def test_simple_remove_tail(simple_dll):
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


def test_middle_remove(simple_dll):
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
