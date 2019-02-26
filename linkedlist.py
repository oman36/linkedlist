class List:
    __slots__ = ['_value', '_next']

    def __init__(self, value, next_: 'List' = None):
        self._value = value
        self._next = next_

    def __iter__(self):
        for l in self._iter():
            yield l._value

    def _iter(self):
        current = self
        while current:
            yield current
            current = current._next

    def print(self, sep: str = ' '):
        """Print all values from self to tail separated by `sep`

        :param sep: string inserted between values, default a space.
        """
        self._print(sep=sep, reversed_=False)

    def get_tail(self):
        """
        :return: last list's element
        """
        head = self
        for head in self._iter():
            pass
        return head

    def append(self, value):
        """Append value to the head of list

        :param value: any value
        """
        self.get_tail()._next = self.__class__(value)

    def __add__(self, other):
        if not isinstance(other, (List, list)):
            return NotImplemented

        root = self._copy()
        current = root.get_tail()
        for v in other:
            current._next = self.__class__(v)
            current = current._next
        return root

    def _copy(self):
        current = root = self.__class__(self._value)
        if self._next is not None:
            for val in self._next:
                current._next = self.__class__(val)
                current = current._next

        return root

    def __reversed__(self):
        if self._next is not None:
            for v in reversed(self._next):
                yield v
        yield self._value

    def _print(self, sep: str, reversed_: bool = False):
        values = reversed(self) if reversed_ else self
        for v in values:
            print(v, end=sep)

    def print_reversed(self, sep: str = ' '):
        """Print all values from tail to self separated by `sep`

        :param sep: string inserted between values, default a space.
        """
        self._print(sep=sep, reversed_=True)
