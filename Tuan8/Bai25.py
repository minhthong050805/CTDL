import math


def hash_multiplication(k, m, A=(math.sqrt(5) - 1) / 2):
    frac = (k * A) % 1
    return math.floor(m * frac)


def hash_division(k, m):
    return k % m


A = (math.sqrt(5) - 1) / 2
m = 16

keys = [123456, 123457, 123458, 654321, 111111, 222222]

print(f"Ty le vang A = {A:.6f}")
print(f"{'khoa':>10} | {'phuong phap nhan':>18} | {'phuong phap chia':>18}")
for k in keys:
    hm = hash_multiplication(k, m, A)
    hd = hash_division(k, m)
    print(f"{k:>10} | {hm:>18} | {hd:>18}")

print()
buckets_mult = [0] * m
buckets_div = [0] * m
for k in range(1, 2001):
    buckets_mult[hash_multiplication(k, m, A)] += 1
    buckets_div[hash_division(k, m)] += 1

print(f"Phan bo 2000 khoa lien tiep (1..2000), m = {m}:")
print(f"  Phuong phap nhan : {buckets_mult}")
print(f"  Phuong phap chia : {buckets_div}")

print()
print("Nhan xet: phuong phap chia (k mod m) rat nhay voi cach chon m va cau truc")
print("cua du lieu dau vao (vi du du lieu tuan tu de gay phan bo khong deu neu m")
print("co uoc chung voi buoc nhay cua du lieu). Phuong phap nhan it phu thuoc vao m hon,")
print("hoat dong tot voi moi gia tri m (khong bat buoc phai la so nguyen to),")
print("va voi A ~ ty le vang thi phan bo thuong deu hon trong thuc te.")
