class List:
    def __init__(self, value, next_: 'List' = None):
        self.value = value
        self.next = next_

    def __iter__(self):
        for l in self._iter():
            yield l.value

    def _iter(self):
        current = self
        while current:
            yield current
            current = current.next

    def print(self, sep: str = ' '):
        """Print all values from self to head separated by `sep`

        :param sep: separator
        """
        self._print(sep=sep, reversed_=False)

    def get_head(self):
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
        self.get_head().next = self.__class__(value)

    def __add__(self, other):
        if not isinstance(other, (List, list)):
            raise TypeError('unsupported operand type(s) for +: \'%s\' and \'%s\'' %
                            (self.__class__, other.__class__))

        root = self.__copy__()
        current = root.get_head()
        for v in other:
            current.next = self.__class__(v)
            current = current.next
        return root

    def __copy__(self):
        current = root = self.__class__(self.value)
        for i, val in enumerate(self):
            if i == 0:
                continue
            current.next = self.__class__(val)
            current = current.next

        return root

    def __reversed__(self):
        return (v for v in reversed([v for v in self]))

    def _print(self, sep: str, reversed_: bool = False):
        values = reversed(self) if reversed_ else self
        print(sep.join(str(v) for v in values))

    def print_reversed(self, sep: str = ' '):
        """Print all values from head to self separated by `sep`

        :param sep: separator
        """
        self._print(sep=sep, reversed_=True)
