a = [5, 1, 4, 2, 8]  # //vidu

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]

print(a)  # [1, 4, 2, 5, 8]
