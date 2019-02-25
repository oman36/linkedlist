import sys
import unittest
from contextlib import contextmanager
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


if __name__ == '__main__':
    unittest.main()
