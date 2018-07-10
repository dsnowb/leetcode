from pytest import fixture
from lfu_cache import DLL, LFUCache


@fixture
def empty_dll():
    return DLL()


@fixture
def single_dll():
    dll = DLL()
    dll.insert(1)
    return dll


@fixture
def simple_dll():
    dll = DLL()
    for i in range(10):
        dll.insert(i)

    return dll


@fixture
def empty_lfu():
    return LFUCache(1)


@fixture
def empty_multi_lfu():
    return LFUCache(10)


@fixture
def single_lfu():
    lfu = LFUCache(1)
    lfu.put(1, 10)
    return lfu


@fixture
def small_lfu():
    lfu = LFUCache(10)
    for i in range(10):
        lfu.put(i, i * 10)

    return lfu
