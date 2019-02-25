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

    def print(self, sep=' '):
        print(sep.join(str(v) for v in self))

    def get_head(self):
        head = self
        for head in self._iter():
            pass
        return head

    def append(self, value):
        self.get_head().next = List(value)
