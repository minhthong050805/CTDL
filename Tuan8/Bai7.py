class RehashingHashTable:
    def __init__(self, capacity=4, load_threshold=0.75):
        self.capacity = capacity
        self.load_threshold = load_threshold
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key, capacity):
        return hash(key) % capacity

    def load_factor(self):
        return self.size / self.capacity

    def put(self, key, value):
        idx = self._index(key, self.capacity)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.load_factor() > self.load_threshold:
            self._rehash()

    def get(self, key):
        idx = self._index(key, self.capacity)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def _rehash(self):
        old_buckets = self.buckets
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in old_buckets:
            for k, v in bucket:
                idx = self._index(k, new_capacity)
                new_buckets[idx].append((k, v))
        print(f"  [Rehash] load factor vuot {self.load_threshold}: "
              f"capacity {self.capacity} -> {new_capacity}")
        self.capacity = new_capacity
        self.buckets = new_buckets

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return str(dict(items))


table = RehashingHashTable(capacity=4, load_threshold=0.75)
for i in range(1, 11):
    table.put(i, i * i)
    print(f"Sau put({i}): size={table.size}, capacity={table.capacity}, "
          f"load_factor={table.load_factor():.2f}")

print(f"Bang bam cuoi cung: {table}")
