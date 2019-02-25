import sys
import unittest
from contextlib import contextmanager
from copy import copy
from io import StringIO

from linkedlist import List


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestListMethods(unittest.TestCase):
    def test_iterator(self):
        original = [1, 2, 3]
        list_ = List(original[0], List(original[1], List(original[2])))
        vals = []
        for v in list_:
            vals.append(v)

        self.assertEqual(vals, original)

    def test_print(self):
        list_ = List(1, List(2, List(3)))
        with captured_output() as (out, err):
            list_.print()
            self.assertEqual(out.getvalue().strip(), '1 2 3')

        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3')

    def test_append(self):
        list_ = List(1, List(2, List(3)))
        list_.append(4)
        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3\t4')

    def test_get_head(self):
        head = List(3)
        list_ = List(1, List(2, head))
        self.assertIs(list_.get_head(), head)
        self.assertIs(head.get_head(), head)

    def test_add(self):
        list_ = List(1, List(2, List(3)))
        tail = List(5, List(6))
        list_ += tail
        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3\t5\t6')
        tail._value = 0
        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3\t5\t6')

    def test_copy(self):
        list_ = List(1, List(2, List(3)))
        list_2 = copy(list_)
        list_2._next._value = 0
        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3')

    def test_add_list(self):
        list_ = List(1, List(2, List(3)))
        simple_list = [5, 6]
        list_ += simple_list
        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3\t5\t6')
        simple_list[0] = 0
        with captured_output() as (out, err):
            list_.print('\t')
            self.assertEqual(out.getvalue().strip(), '1\t2\t3\t5\t6')

    def test_print_reversed(self):
        list_ = List(1, List(2, List(3)))
        with captured_output() as (out, err):
            list_.print_reversed('\t')
            self.assertEqual(out.getvalue().strip(), '3\t2\t1')

    def test_reverse(self):
        list_ = List(1, List(2, List(3)))
        values = []
        for v in reversed(list_):
            values.append(v)
        self.assertEqual(values, [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
