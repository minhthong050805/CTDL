a = [3, 1, 4, 1, 5]  # //vidu
k = 2                 # //vidu

n = len(a)
for i in range(k):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a) 
