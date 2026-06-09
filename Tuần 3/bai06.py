a = [4, 2, 7, 1, 3]  # //vidu

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]

print(a[-1])  # 7
