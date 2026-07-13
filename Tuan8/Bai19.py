def count_collisions(keys, hash_fn, m):
    buckets = {}
    for k in keys:
        idx = hash_fn(k) % m
        buckets.setdefault(idx, []).append(k)
    collisions = 0
    for idx, ks in buckets.items():
        if len(ks) > 1:
            collisions += len(ks) - 1
    return collisions, buckets


def bad_hash(k):
    return k * 100


def good_hash(k):
    return (k * 2654435761) & 0xFFFFFFFF


keys = list(range(20))
m = 16

bad_collisions, bad_buckets = count_collisions(keys, bad_hash, m)
good_collisions, good_buckets = count_collisions(keys, good_hash, m)

print(f"Tap khoa: {keys}, so bucket m = {m}")
print(f"Ham bam kem (k*100 mod m): so va cham = {bad_collisions}")
for idx in sorted(bad_buckets):
    if len(bad_buckets[idx]) > 1:
        print(f"  bucket {idx}: {bad_buckets[idx]}")

print()
print(f"Ham bam tot (nhan hang so lon, mod m): so va cham = {good_collisions}")
for idx in sorted(good_buckets):
    if len(good_buckets[idx]) > 1:
        print(f"  bucket {idx}: {good_buckets[idx]}")

print()
print("Nhan xet: so va cham cang thap thi chat luong phan bo cua ham bam cang tot.")
