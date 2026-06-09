a = [1, 2, 3]  # //vidu

n = len(a)
cmp = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        cmp += 1
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)    # [1, 2, 3]
print(cmp)  # 3
