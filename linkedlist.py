class List:
    def __init__(self, value, next_: 'List' = None):
        self.value = value
        self.next = next_

    def __iter__(self):
        current = self
        while current:
            yield current.value
            current = current.next

    def print(self, sep=' '):
        print(sep.join(str(v) for v in self))