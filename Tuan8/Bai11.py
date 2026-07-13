class MyHashSet:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _index(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        idx = self._index(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)
            self.size += 1

    def contains(self, key):
        idx = self._index(key)
        return key in self.buckets[idx]

    def remove(self, key):
        idx = self._index(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)
            self.size -= 1

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return "{" + ", ".join(str(x) for x in sorted(items)) + "}"


s = MyHashSet()
for x in [1, 1, 2]:
    s.add(x)
print(f"Sau khi add(1,1,2): {s}")
print(f"contains(1) = {s.contains(1)}")
print(f"contains(3) = {s.contains(3)}")
s.remove(1)
print(f"Sau khi remove(1): {s}")
print(f"contains(1) = {s.contains(1)}")
