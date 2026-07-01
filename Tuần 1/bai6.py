def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

a = list(map(int, input("Nhap mang (cach nhau boi dau cach): ").split()))
x = int(input("Nhap x can tim: "))
ket_qua = linear_search(a, x)
print("Ket qua:", ket_qua)
