from unittest import TestCase
from Collection import Collection


class TestCollection(TestCase):
    def test_init(self):
        col = Collection([1, 2])
        self.assertEqual([1, 2], col.array)

    def test_get_collection(self):
        array = Collection([1, 2])
        self.assertEqual([1, 2], array.get_collection())

    def test_add(self):
        col = Collection([])
        self.assertRaises(NotImplementedError, col.add, 1, 2)

    def test_getitem(self):
        array = Collection([False, "nicole", 1, 3.2])
        self.assertEqual("nicole", array[1])
        self.assertEqual(None, array[5])

    def test_eq(self):
        array = Collection([1])
        other1 = Collection([1])
        other2 = int
        other3 = Collection([1, 2])
        self.assertEqual(True, array == other1)
        self.assertEqual(False, array == other2)
        self.assertEqual(False, array == other3)

    def test_ne(self):
        array = Collection([1])
        other1 = Collection([1])
        other2 = int
        other3 = Collection([1, 2])
        self.assertEqual(False, array != other1)
        self.assertEqual(True, array != other2)
        self.assertEqual(True, array != other3)

    def test_len(self):
        array = Collection([1, "nicole", True])
        self.assertEqual(3, len(array))

    def test_contains(self):
        array = Collection([1, "nicole", True])
        item1 = True
        item2 = 2
        self.assertEqual(True, item1 in array)
        self.assertEqual(False, item2 in array)

    def test_str(self):
        array = Collection([1, "nicole", True])
        self.assertEqual('1nicoleTrue', array.__str__())

    def test_repr(self):
        array = Collection([1, "nicole", True])
        self.assertEqual('1nicoleTrue', array.__repr__())

