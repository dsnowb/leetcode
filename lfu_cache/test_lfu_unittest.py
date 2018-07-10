from lfu_cache import Node, DLL
from unittest import TestCase, main


class TestDLL(TestCase):
    """
    Unit tests for DLL.
    """
    def setUp(self):
        self.empty_dll = DLL()
        self.single_dll = DLL()
        self.single_dll.insert(1)

    def test_dll_instance(self):
        self.assertEqual(len(self.empty_dll), self.empty_dll.length)

    def test_dll_single_insert(self):
        self.empty_dll.insert(1)

        self.assertIs(self.empty_dll.head, self.empty_dll.tail)
        self.assertIsInstance(self.empty_dll.head, Node)


if __name__ == '__main__':
    main()
