data = [(2, 'x1'), (1, 'y'), (2, 'x2'), (1, 'z'), (2, 'x3')]  # //vidu
a = data[:]
n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j][0] > a[j + 1][0]:  
            a[j], a[j + 1] = a[j + 1], a[j]
ket_qua_bubble = a
b = data[:]
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if b[j][0] < b[min_idx][0]:
            min_idx = j
    b[i], b[min_idx] = b[min_idx], b[i]
ket_qua_selection = b

print("Bubble (ổn định):     ", ket_qua_bubble)
print("Selection (không ổn):", ket_qua_selection)
print("Kết quả khác nhau:   ", ket_qua_bubble != ket_qua_selection)  
