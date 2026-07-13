import time
import random


class VulnerableHashTable:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _weak_hash(self, key):
        return sum(ord(c) for c in key) % self.capacity

    def put(self, key, value):
        idx = self._weak_hash(key)
        self.buckets[idx].append((key, value))

    def get(self, key):
        idx = self._weak_hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)


class SecureHashTable:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.secret = random.randint(1, 2**31 - 1)

    def _keyed_hash(self, key):
        h = self.secret
        for c in key:
            h = ((h * 131) + ord(c) + self.secret) & 0xFFFFFFFF
        return h % self.capacity

    def put(self, key, value):
        idx = self._keyed_hash(key)
        self.buckets[idx].append((key, value))

    def get(self, key):
        idx = self._keyed_hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)


def generate_colliding_keys(target_sum, count):
    keys = []
    for i in range(count):
        length = 2
        base = target_sum // length
        rem = target_sum - base * length
        s = chr(base) * (length - 1) + chr(base + rem)
        keys.append(s + str(i))
    return keys


N = 3000
malicious_keys = [f"key{i}" for i in range(N)]
malicious_keys_same_bucket = [chr(97) * 2 + str(i) for i in range(N)]

vuln = VulnerableHashTable(capacity=1024)
t0 = time.perf_counter()
for k in malicious_keys_same_bucket:
    vuln.put(k, 1)
t_insert_vuln = time.perf_counter() - t0

secure = SecureHashTable(capacity=1024)
t0 = time.perf_counter()
for k in malicious_keys_same_bucket:
    secure.put(k, 1)
t_insert_secure = time.perf_counter() - t0

vuln_bucket_sizes = [len(b) for b in vuln.buckets]
secure_bucket_sizes = [len(b) for b in secure.buckets]

print(f"So khoa doc hai chen vao: {N}")
print(f"Bang bam de bi tan cong (ham bam khong co khoa bi mat):")
print(f"  Thoi gian chen: {t_insert_vuln:.4f}s")
print(f"  Bucket lon nhat chua: {max(vuln_bucket_sizes)} phan tu")
print()
print(f"Bang bam duoc bao ve (keyed hash voi secret ngau nhien):")
print(f"  Thoi gian chen: {t_insert_secure:.4f}s")
print(f"  Bucket lon nhat chua: {max(secure_bucket_sizes)} phan tu")
print()
print("Nhan xet: voi ham bam co the doan truoc (khong co secret), ke tan cong")
print("co the co y tao hang loat khoa cung roi vao mot bucket, bien thao tac")
print("O(1) trung binh thanh O(n), gay tu choi dich vu (DoS).")
print("Cach phong chong: dung ham bam co khoa bi mat (keyed hash / SipHash)")
print("duoc khoi tao ngau nhien moi lan chay chuong trinh, khien ke tan cong")
print("khong the du doan truoc bucket dich de tao va cham co y.")
