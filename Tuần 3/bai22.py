import random, time

random.seed(1)
n = 10000
k = 3  # //vidu
a = []
base = list(range(n))
i = 0
while i < n:
    chunk = base[i:i + k + 1]
    random.shuffle(chunk)
    a.extend(chunk)
    i += k + 1
a = a[:n]
b = a[:]
t0 = time.time()
so_luot = 0
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            swapped = True
    so_luot += 1
    if not swapped:
        break
t1 = time.time()

print(f"n = {n}, k = {k}")
print(f"Số lượt thực tế: {so_luot}  (lý thuyết ≤ {k} lượt do độ lệch tối đa {k})")
print(f"Thời gian: {(t1 - t0)*1000:.1f}ms")
print(f"Đúng: {b == sorted(a)}")
