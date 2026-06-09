a = [-3, 1, -2, 2]  # //vidu

n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if abs(a[j]) > abs(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)  
