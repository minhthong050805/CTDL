class QuadraticProbingTable:
    EMPTY = object()

    def __init__(self, capacity=11):
        self.capacity = capacity
        self.keys = [self.EMPTY] * capacity
        self.values = [None] * capacity
        self.probes_log = []

    def put(self, key, value):
        idx = hash(key) % self.capacity
        i = 0
        probes = 0
        while True:
            probe = (idx + i * i) % self.capacity
            probes += 1
            if self.keys[probe] is self.EMPTY or self.keys[probe] == key:
                self.keys[probe] = key
                self.values[probe] = value
                self.probes_log.append(probes)
                return
            i += 1
            if i > self.capacity:
                raise Exception("Bang day, khong the chen them")

    def get(self, key):
        idx = hash(key) % self.capacity
        i = 0
        while i <= self.capacity:
            probe = (idx + i * i) % self.capacity
            if self.keys[probe] is self.EMPTY:
                raise KeyError(key)
            if self.keys[probe] == key:
                return self.values[probe]
            i += 1
        raise KeyError(key)


class DoubleHashingTable:
    EMPTY = object()

    def __init__(self, capacity=11):
        self.capacity = capacity
        self.keys = [self.EMPTY] * capacity
        self.values = [None] * capacity
        self.probes_log = []

    def _h2(self, key):
        return 1 + (hash(key) % (self.capacity - 1))

    def put(self, key, value):
        idx = hash(key) % self.capacity
        step = self._h2(key)
        i = 0
        probes = 0
        while True:
            probe = (idx + i * step) % self.capacity
            probes += 1
            if self.keys[probe] is self.EMPTY or self.keys[probe] == key:
                self.keys[probe] = key
                self.values[probe] = value
                self.probes_log.append(probes)
                return
            i += 1
            if i > self.capacity:
                raise Exception("Bang day, khong the chen them")

    def get(self, key):
        idx = hash(key) % self.capacity
        step = self._h2(key)
        i = 0
        while i <= self.capacity:
            probe = (idx + i * step) % self.capacity
            if self.keys[probe] is self.EMPTY:
                raise KeyError(key)
            if self.keys[probe] == key:
                return self.values[probe]
            i += 1
        raise KeyError(key)


class LinearProbingTable:
    EMPTY = object()

    def __init__(self, capacity=11):
        self.capacity = capacity
        self.keys = [self.EMPTY] * capacity
        self.values = [None] * capacity
        self.probes_log = []

    def put(self, key, value):
        idx = hash(key) % self.capacity
        probes = 0
        for i in range(self.capacity):
            probe = (idx + i) % self.capacity
            probes += 1
            if self.keys[probe] is self.EMPTY or self.keys[probe] == key:
                self.keys[probe] = key
                self.values[probe] = value
                self.probes_log.append(probes)
                return


keys_to_insert = [17, 34, 51, 68, 85, 102, 119]

linear = LinearProbingTable(capacity=17)
quad = QuadraticProbingTable(capacity=17)
dbl = DoubleHashingTable(capacity=17)

for k in keys_to_insert:
    linear.put(k, k)
    quad.put(k, k)
    dbl.put(k, k)

print(f"Cac khoa chen vao: {keys_to_insert} (deu dong du 0 mod 17 -> gay va cham)")
print(f"So lan do (probes) moi lan chen - Linear Probing : {linear.probes_log}, "
      f"tong = {sum(linear.probes_log)}")
print(f"So lan do (probes) moi lan chen - Quadratic Probing: {quad.probes_log}, "
      f"tong = {sum(quad.probes_log)}")
print(f"So lan do (probes) moi lan chen - Double Hashing   : {dbl.probes_log}, "
      f"tong = {sum(dbl.probes_log)}")
print()
print("Nhan xet: voi cac khoa dong du (cung idx ban dau), Linear Probing chiem")
print("cac o LIEN TIEP nhau, gay gom cum chinh (primary clustering) ro ret -")
print("cac khoa chen sau se lai va cham voi ca cum nay.")
print("Quadratic Probing dung cung so lan do nhung cac o duoc chon KHONG lien")
print("tiep nhau (rai theo i^2), nen giam duoc gom cum chinh, du van co the gap")
print("gom cum thu cap (secondary clustering) giua cac khoa cung idx ban dau.")
print("Double Hashing cho so lan do trung binh THAP NHAT vi buoc nhay phu thuoc")
print("vao ban than khoa, cac khoa dong du se do theo cac buoc nhay khac nhau,")
print("gan nhu loai bo hoan toan hien tuong gom cum.")
