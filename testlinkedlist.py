import unittest

from linkedlist import List


class TestListMethods(unittest.TestCase):
    def test_iterator(self):
        original = [1, 2, 3]
        list_ = List(original[0], List(original[1], List(original[2])))
        vals = []
        for v in list_:
            vals.append(v)

        self.assertEqual(vals, original)


if __name__ == '__main__':
    unittest.main()
