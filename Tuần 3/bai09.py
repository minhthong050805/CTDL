a = [1, 2, 3, 4]  # //vidu

n = len(a)
so_luot = 0
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True
    so_luot += 1
    if not swapped:
        break

print(a)        
print(so_luot) 
