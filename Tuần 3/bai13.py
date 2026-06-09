a = [(2, 'a'), (1, 'b'), (2, 'c')]  # //vidu

n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j][0] > a[j + 1][0]: 
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)  
nhan_key2 = [item[1] for item in a if item[0] == 2]
print(nhan_key2 == ['a', 'c']) 
