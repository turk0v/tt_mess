import unittest
from DoubleLinked_list import Item, DoubleLinkedList


class ExpectedFailureTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_delete_no_elem(self):
        list = DoubleLinkedList()
        self.assertEqual(list.delete(1), 'broken')

    @unittest.expectedFailure
    def test_contains_no_elem(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        self.assertEqual(list.contains(6), 'broken')


class TestDoubleLinkedList(unittest.TestCase):

    def test_len(self):
        list = DoubleLinkedList()
        for i in range(100):
            list.push(i)
        self.assertEqual(list.len(), 100)

    def test_len_zero_list(self):
        list = DoubleLinkedList()
        self.assertEqual(list.len(), 0)

    def test_delete(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        list.delete(4)
        self.assertEqual(list.dl_to_list(), [0, 1, 2, 3])

    def test_contains(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        self.assertEqual(list.contains(1), True)

    def test_contains_zero_list(self):
        list = DoubleLinkedList()
        self.assertEqual(list.contains(1), False)

    def test_first_last(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        self.assertEqual(list.first(), 0)
        self.assertEqual(list.last(), 4)

    def test_first_last_one_item_list(self):
        list = DoubleLinkedList()
        for i in range(1):
            list.push(i)
        self.assertEqual(list.first(), 0)
        self.assertEqual(list.last(), 0)

    def test_first_last_zero_list(self):
        list = DoubleLinkedList()
        self.assertEqual(list.first(), 'empty DoubleLinked')
        self.assertEqual(list.last(), 'empty DoubleLinked')

    def test_unshift(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        list.unshift(6)
        self.assertEqual(list.dl_to_list(), [6, 0, 1, 2, 3, 4])

    def test_shift(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        list.shift()
        self.assertEqual(list.dl_to_list(), [1, 2, 3, 4])

    def test_shift_zero_list(self):
        list = DoubleLinkedList()
        self.assertEqual(list.shift(), 'empty DoubleLinked')

    def test_push(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        self.assertEqual(list.dl_to_list(), [0, 1, 2, 3, 4])

    def test_pop(self):
        list = DoubleLinkedList()
        for i in range(5):
            list.push(i)
        list.pop()
        self.assertEqual(list.dl_to_list(), [0, 1, 2, 3])

    def test_pop_zero_list(self):
        list = DoubleLinkedList()
        self.assertEqual(list.pop(), 'empty DoubleLinked')

    def test_pop_one_item(self):
        list = DoubleLinkedList()
        for i in range(1):
            list.push(i)
        list.pop()
        self.assertEqual(list.dl_to_list(), [])


if __name__ == '__main__':
    unittest.main()
