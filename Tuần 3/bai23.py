import random
from tabulate import tabulate

n = 500

random.seed(0)
ngau_nhien  = random.sample(range(n), n)         # //vidu ngẫu nhiên
da_sap_xep  = list(range(n))                      # //vidu đã sắp xếp
nguoc_thu_tu = list(range(n - 1, -1, -1))         # //vidu sắp xếp ngược

results = []

for ten, arr in [("Ngẫu nhiên", ngau_nhien),
                 ("Đã sắp xếp", da_sap_xep),
                 ("Ngược thứ tự", nguoc_thu_tu)]:
    a = arr[:]
    cmps = swaps = passes = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            cmps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        passes += 1
        if not swapped:
            break
    results.append([ten, cmps, swaps, passes])

print(tabulate(results, headers=["Đầu vào", "Số so sánh", "Số swap", "Số lượt"]))
