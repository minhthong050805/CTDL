class LinearProbingHashTable:
    EMPTY = object()
    DELETED = object()

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.keys = [self.EMPTY] * self.capacity
        self.values = [None] * self.capacity

    def _index(self, key):
        return hash(key) % self.capacity

    def _find_slot(self, key):
        idx = self._index(key)
        first_deleted = None
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                return first_deleted if first_deleted is not None else probe
            if self.keys[probe] is self.DELETED:
                if first_deleted is None:
                    first_deleted = probe
                continue
            if self.keys[probe] == key:
                return probe
        return first_deleted

    def put(self, key, value):
        if self.size >= self.capacity * 0.7:
            self._resize()
        slot = self._find_slot(key)
        if self.keys[slot] is self.EMPTY or self.keys[slot] is self.DELETED:
            self.size += 1
        self.keys[slot] = key
        self.values[slot] = value

    def get(self, key):
        idx = self._index(key)
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                raise KeyError(key)
            if self.keys[probe] is self.DELETED:
                continue
            if self.keys[probe] == key:
                return self.values[probe]
        raise KeyError(key)

    def remove(self, key):
        idx = self._index(key)
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                raise KeyError(key)
            if self.keys[probe] is not self.DELETED and self.keys[probe] == key:
                self.keys[probe] = self.DELETED
                self.values[probe] = None
                self.size -= 1
                return
        raise KeyError(key)

    def _resize(self):
        old_keys, old_values = self.keys, self.values
        self.capacity *= 2
        self.keys = [self.EMPTY] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        for k, v in zip(old_keys, old_values):
            if k is not self.EMPTY and k is not self.DELETED:
                self.put(k, v)

    def __repr__(self):
        items = {}
        for k, v in zip(self.keys, self.values):
            if k is not self.EMPTY and k is not self.DELETED:
                items[k] = v
        return str(items)


table = LinearProbingHashTable(capacity=8)
for k, v in [(1, 'A'), (9, 'B'), (17, 'C'), (2, 'D')]:
    idx = table._index(k)
    print(f"put({k}) -> chi so ban dau {idx}")
    table.put(k, v)

print(f"Bang sau khi them: {table}")
print(f"get(9) = {table.get(9)}")
table.remove(9)
print(f"Sau khi remove(9): {table}")
print(f"get(17) van dung vi da dung tombstone: {table.get(17)}")
