import random


def hash_bad(k, m):
    return (k * 4) % m


def hash_good(k, m):
    return (k * 2654435761) % (2**32) % m


def chi_square(keys, hash_fn, m):
    buckets = [0] * m
    for k in keys:
        buckets[hash_fn(k, m)] += 1
    expected = len(keys) / m
    chi2 = sum((count - expected) ** 2 / expected for count in buckets)
    return chi2, buckets


random.seed(42)
keys = [random.randint(1, 10**6) * 4 for _ in range(2000)]
m = 64

chi2_bad, buckets_bad = chi_square(keys, hash_bad, m)
chi2_good, buckets_good = chi_square(keys, hash_good, m)

print(f"So khoa kiem tra: {len(keys)}, so bucket m = {m}")
print(f"Chi-square cua ham bam kem (k*4 mod m): {chi2_bad:.2f}")
print(f"  So bucket rong: {sum(1 for c in buckets_bad if c == 0)}")
print(f"Chi-square cua ham bam tot (nhan hang so lon roi mod m): {chi2_good:.2f}")
print(f"  So bucket rong: {sum(1 for c in buckets_good if c == 0)}")

print()
if chi2_bad > chi2_good:
    print("Ket luan: ham bam tot co chi-square nho hon, cho thay phan bo")
    print("cac phan tu vao bucket deu hon (gan phan phoi deu ly tuong).")
else:
    print("Ket luan: trong truong hop nay ca hai ham co do lech tuong duong.")
