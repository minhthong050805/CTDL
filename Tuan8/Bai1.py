class ChainingHashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key):
        idx = self._index(key)
        return any(k == key for k, v in self.buckets[idx])

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return str(dict(items))


table = ChainingHashTable()
table.put('a', 1)
table.put('b', 2)
table.put('c', 3)
print(f"get('a') = {table.get('a')}")
print(f"get('b') = {table.get('b')}")
print(f"Bang bam hien tai: {table}")
table.put('a', 100)
print(f"Sau khi cap nhat put('a', 100): get('a') = {table.get('a')}")
table.remove('b')
print(f"Sau khi remove('b'): {table}")
print(f"'b' in table = {'b' in table}")
