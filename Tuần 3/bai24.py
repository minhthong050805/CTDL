truoc = [4, 3, 2, 1]  # //vidu
sau   = [3, 2, 1, 4]  # //vidu

n = len(truoc)
so_luot = -1

for k in range(n + 1):
    a = truoc[:]
    for i in range(k):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    if a == sau:
        so_luot = k
        break

print(f"Số lượt tối thiểu: {so_luot}")  
