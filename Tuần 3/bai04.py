a = [3, 2, 1]  # //vidu

n = len(a)
count = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            count += 1

print(a)      # [1, 2, 3]
print(count)  # 3
