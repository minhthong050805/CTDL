class LazyDeleteHashTable:
    EMPTY = object()
    DELETED = object()

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.keys = [self.EMPTY] * capacity
        self.values = [None] * capacity
        self.size = 0
        self.tombstones = 0

    def put(self, key, value):
        idx = hash(key) % self.capacity
        first_deleted = None
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                slot = first_deleted if first_deleted is not None else probe
                if self.keys[slot] is self.DELETED:
                    self.tombstones -= 1
                self.keys[slot] = key
                self.values[slot] = value
                self.size += 1
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
                self.tombstones += 1
                return
        raise KeyError(key)

    def needs_cleanup(self, threshold=0.3):
        return self.tombstones / self.capacity > threshold

    def cleanup(self):
        old_keys, old_values = self.keys, self.values
        self.keys = [self.EMPTY] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        self.tombstones = 0
        for k, v in zip(old_keys, old_values):
            if k is not self.EMPTY and k is not self.DELETED:
                self.put(k, v)


table = LazyDeleteHashTable(capacity=8)
for k in [1, 9, 17, 25]:
    table.put(k, f"val{k}")

print(f"Truoc khi xoa: keys = {[k if k is not table.EMPTY else '-' for k in table.keys]}")
table.remove(9)
table.remove(17)
print(f"Sau khi remove(9), remove(17): "
      f"keys = {[k if (k is not table.EMPTY and k is not table.DELETED) else ('X' if k is table.DELETED else '-') for k in table.keys]}")
print(f"get(25) van tim duoc dung vi chuoi do khong bi dut: {table.get(25)}")
print(f"So tombstone hien tai: {table.tombstones}")
print(f"Can don dep lai bang (>30% tombstone)? {table.needs_cleanup(0.2)}")
table.cleanup()
print("Da goi cleanup() de xay dung lai bang, loai bo toan bo tombstone.")
print(f"So tombstone sau cleanup: {table.tombstones}")
print()
print("Thao luan: Xoa that trong open addressing se de lai 'lo hong' EMPTY,")
print("lam dut chuoi do tim (probe sequence), khien cac phan tu chen sau do")
print("qua cung bucket bi that lac. Dung nhan DELETED (tombstone) giu chuoi do")
print("nguyen ven. Can don dep lai bang (rehash toan bo, bo tombstone) khi")
print("ty le tombstone qua cao, vi tombstone lam thao tac get/put phai do qua")
print("nhieu o hon binh thuong, lam giam hieu nang theo thoi gian.")
