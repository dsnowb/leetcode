from pytest import fixture
from lfu_cache import Node, DLL, LFUCache


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
