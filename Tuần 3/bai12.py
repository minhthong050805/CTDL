a = ['abc', 'a', 'ab']  # //vidu

n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(a[j]) > len(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)  
