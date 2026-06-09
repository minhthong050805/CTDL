a = [5, 1, 4, 2, 8]  # //vidu

n = len(a)
left = 0
right = n - 1
so_luot = 0

while left < right:
    for i in range(left, right):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    right -= 1

    for i in range(right, left, -1):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
    left += 1
    so_luot += 1

print(a)        
print(so_luot)  
