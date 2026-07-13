import math
import hashlib


class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [0] * size

    def _hashes(self, item):
        item_bytes = str(item).encode()
        h1 = int(hashlib.md5(item_bytes).hexdigest(), 16)
        h2 = int(hashlib.sha1(item_bytes).hexdigest(), 16)
        for i in range(self.num_hashes):
            yield (h1 + i * h2) % self.size

    def add(self, item):
        for idx in self._hashes(item):
            self.bits[idx] = 1

    def might_contain(self, item):
        return all(self.bits[idx] == 1 for idx in self._hashes(item))

    @staticmethod
    def optimal_params(n, false_positive_rate):
        m = -(n * math.log(false_positive_rate)) / (math.log(2) ** 2)
        k = (m / n) * math.log(2)
        return math.ceil(m), max(1, round(k))


n_items = 1000
target_fp = 0.01
m, k = BloomFilter.optimal_params(n_items, target_fp)
print(f"So phan tu du kien n = {n_items}, ty le duong tinh gia mong muon = {target_fp}")
print(f"Kich thuoc bit toi uu m = {m}, so ham bam toi uu k = {k}")

bf = BloomFilter(size=m, num_hashes=k)
inserted = [f"user_{i}" for i in range(n_items)]
for item in inserted:
    bf.add(item)

false_positives = 0
test_count = 5000
not_inserted = [f"guest_{i}" for i in range(test_count)]
for item in not_inserted:
    if bf.might_contain(item):
        false_positives += 1

print()
print(f"Kiem tra {n_items} phan tu da them: tat ca deu bao 'co' "
      f"= {all(bf.might_contain(x) for x in inserted)}")
print(f"Kiem tra {test_count} phan tu KHONG them vao: "
      f"so lan bao nham 'co' (duong tinh gia) = {false_positives}")
print(f"Ty le duong tinh gia thuc te = {false_positives / test_count:.4f} "
      f"(ly thuyet ~ {target_fp})")
print()
print("Bloom filter khong bao gio bao 'khong' nham (khong am tinh gia),")
print("nhung co the bao 'co' nham (duong tinh gia) do va cham bit giua nhieu phan tu.")
