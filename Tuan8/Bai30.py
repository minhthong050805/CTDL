import random


def true_jaccard(a, b):
    set_a, set_b = set(a), set(b)
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union else 0.0


class MinHash:
    def __init__(self, num_hashes=100, seed=42):
        rng = random.Random(seed)
        self.num_hashes = num_hashes
        self.p = (1 << 61) - 1
        self.a = [rng.randint(1, self.p - 1) for _ in range(num_hashes)]
        self.b = [rng.randint(0, self.p - 1) for _ in range(num_hashes)]

    def signature(self, s):
        sig = [float('inf')] * self.num_hashes
        for item in s:
            x = hash(item) & 0xFFFFFFFFFFFFFFFF
            for i in range(self.num_hashes):
                h = ((self.a[i] * x + self.b[i]) % self.p)
                if h < sig[i]:
                    sig[i] = h
        return sig

    def estimate_similarity(self, sig_a, sig_b):
        equal = sum(1 for x, y in zip(sig_a, sig_b) if x == y)
        return equal / self.num_hashes


random.seed(1)
universe = [f"word_{i}" for i in range(1000)]
set_a = set(random.sample(universe, 300))
set_b = (set_a - set(random.sample(list(set_a), 100))) | set(random.sample(universe, 100))

real_jaccard = true_jaccard(set_a, set_b)

mh = MinHash(num_hashes=200)
sig_a = mh.signature(set_a)
sig_b = mh.signature(set_b)
estimated_jaccard = mh.estimate_similarity(sig_a, sig_b)

print(f"So phan tu tap A: {len(set_a)}, tap B: {len(set_b)}")
print(f"Do tuong dong Jaccard THUC TE (|A giao B| / |A hop B|) = {real_jaccard:.4f}")
print(f"Do tuong dong Jaccard UOC LUONG bang MinHash "
      f"(voi {mh.num_hashes} ham bam) = {estimated_jaccard:.4f}")
print(f"Sai so tuyet doi = {abs(real_jaccard - estimated_jaccard):.4f}")
