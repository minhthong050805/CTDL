import sys
import time
import random


class ChainingTable:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def put(self, key, value):
        idx = hash(key) % self.capacity
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        idx = hash(key) % self.capacity
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = hash(key) % self.capacity
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)

    def memory_bytes(self):
        total = sys.getsizeof(self.buckets)
        for bucket in self.buckets:
            total += sys.getsizeof(bucket)
            for item in bucket:
                total += sys.getsizeof(item)
        return total


class OpenAddressingTable:
    EMPTY = object()
    DELETED = object()

    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.keys = [self.EMPTY] * capacity
        self.values = [None] * capacity
        self.size = 0

    def put(self, key, value):
        idx = hash(key) % self.capacity
        first_deleted = None
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                slot = first_deleted if first_deleted is not None else probe
                if self.keys[slot] is not key:
                    self.size += 1
                self.keys[slot] = key
                self.values[slot] = value
                return
            if self.keys[probe] is self.DELETED:
                if first_deleted is None:
                    first_deleted = probe
                continue
            if self.keys[probe] == key:
                self.values[probe] = value
                return

    def get(self, key):
        idx = hash(key) % self.capacity
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                raise KeyError(key)
            if self.keys[probe] is not self.DELETED and self.keys[probe] == key:
                return self.values[probe]
        raise KeyError(key)

    def remove(self, key):
        idx = hash(key) % self.capacity
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

    def memory_bytes(self):
        return sys.getsizeof(self.keys) + sys.getsizeof(self.values)


def benchmark(table_cls, n, capacity):
    table = table_cls(capacity)
    keys = list(range(n))
    random.shuffle(keys)

    t0 = time.perf_counter()
    for k in keys:
        table.put(k, k * 2)
    t_insert = time.perf_counter() - t0

    t0 = time.perf_counter()
    for k in keys:
        table.get(k)
    t_get = time.perf_counter() - t0

    return table, t_insert, t_get


N = 5000
CAPACITY_LOW_LOAD = 16384
CAPACITY_HIGH_LOAD = 6000

print("So sanh voi he so tai THAP (capacity = 16384, load ~ 0.30):")
for cls, name in [(ChainingTable, "Chaining"), (OpenAddressingTable, "Open Addressing")]:
    table, t_ins, t_get = benchmark(cls, N, CAPACITY_LOW_LOAD)
    print(f"  {name}: insert={t_ins:.4f}s, get={t_get:.4f}s, memory~{table.memory_bytes()} bytes")

print()
print("So sanh voi he so tai CAO (capacity = 6000, load ~ 0.83):")
for cls, name in [(ChainingTable, "Chaining"), (OpenAddressingTable, "Open Addressing")]:
    table, t_ins, t_get = benchmark(cls, N, CAPACITY_HIGH_LOAD)
    print(f"  {name}: insert={t_ins:.4f}s, get={t_get:.4f}s, memory~{table.memory_bytes()} bytes")

print()
print("Nhan xet:")
print("Chaining giu hieu nang gan nhu khong doi khi he so tai tang, vi moi bucket")
print("chi la mot danh sach lien ket rieng le, chi phi tang tuyen tinh theo so phan tu/bucket.")
print("Open addressing suy giam manh khi he so tai cao do hien tuong gom cum (clustering),")
print("phai do qua nhieu o lien tiep de tim cho trong.")
print("Ve bo nho: Open addressing gon hon vi chi dung 2 mang lien tuc, khong co")
print("overhead cua cac node/list rieng le nhu chaining.")
print("Ve xoa: chaining xoa truc tiep phan tu khoi danh sach lien ket, don gian.")
print("Open addressing phai dung xoa lazy (tombstone) vi xoa that se lam dut chuoi do tim,")
print("khien cac gia tri phia sau tro nen khong the truy cap duoc.")
