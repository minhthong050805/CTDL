def linearsearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(value)

x = int(input("nhap gia tri can tim "))

kq = linearsearch(a, x)

if kq != -1:
    print("tim thay tai vi tri",kq)
else:
    print("khong tim thay ")