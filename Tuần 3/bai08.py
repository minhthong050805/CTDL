a = [3, 2, 1]  # //vidu
k = 1          # //vidu

n = len(a)
for _ in range(k):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

da_sap_xep = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        da_sap_xep = False
        break

print(da_sap_xep)  
