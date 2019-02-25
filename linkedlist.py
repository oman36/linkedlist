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
        print(sep.join(str(v) for v in self))

    def get_head(self):
        head = self
        for head in self._iter():
            pass
        return head

    def append(self, value):
        self.get_head().next = self.__class__(value)

    def __add__(self, other):
        if not isinstance(other, List):
            raise TypeError('unsupported operand type(s) for +: \'%s\' and \'%s\'' %
                            (self.__class__, other.__class__))

        root = self.__copy__()
        root.get_head().next = other.__copy__()
        return root

    def __copy__(self):
        current = root = self.__class__(self.value)
        for i, val in enumerate(self):
            if i == 0:
                continue
            current.next = self.__class__(val)
            current = current.next

        return root
