import random


class UniversalHash:
    def __init__(self, m, p=2**61 - 1):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def __call__(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


m = 10
h1 = UniversalHash(m)
h2 = UniversalHash(m)

keys = [3, 17, 42, 99, 256, 1024]

print(f"Ham bam phổ quát 1 (a={h1.a % 1000}..., b={h1.b % 1000}...):")
for k in keys:
    print(f"  h1({k}) = {h1(k)}")

print(f"Ham bam phổ quát 2 (a={h2.a % 1000}..., b={h2.b % 1000}...):")
for k in keys:
    print(f"  h2({k}) = {h2(k)}")

print()
print("Giai thich chong tan cong: vi a, b duoc chon ngau nhien moi lan khoi tao,")
print("ke tan cong khong the biet truoc ham bam cu the de co y tao ra mot loat")
print("khoa cung roi vao mot bucket (tan cong hash flooding). Voi ho ham bam")
print("phổ quát, xac suat hai khoa bat ky va cham la <= 1/m bat ke du lieu dau vao,")
print("nen khong co du lieu 'xau' co dinh nao co the lam suy bien bang bam.")
