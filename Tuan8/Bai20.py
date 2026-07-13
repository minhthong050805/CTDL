def distribution_stats(keys, m):
    buckets = [0] * m
    for k in keys:
        buckets[k % m] += 1
    used = sum(1 for c in buckets if c > 0)
    max_count = max(buckets)
    return buckets, used, max_count


keys = [i * 16 for i in range(1, 51)]

m1 = 16
m2 = 17

buckets1, used1, max1 = distribution_stats(keys, m1)
buckets2, used2, max2 = distribution_stats(keys, m2)

print(f"Tap khoa la boi so cua 16: {keys[:10]}... (tong {len(keys)} khoa)")
print()
print(f"m = {m1} (luy thua cua 2):")
print(f"  Phan bo: {buckets1}")
print(f"  So bucket duoc su dung: {used1}/{m1}")
print(f"  So phan tu dong nhieu nhat trong 1 bucket: {max1}")

print()
print(f"m = {m2} (so nguyen to):")
print(f"  Phan bo: {buckets2}")
print(f"  So bucket duoc su dung: {used2}/{m2}")
print(f"  So phan tu dong nhieu nhat trong 1 bucket: {max2}")

print()
print("Giai thich: khi cac khoa co dang boi so cua mot uoc chung voi m,")
print("vi du m=16=2^4 va khoa la boi cua 16, thi k mod m luon bang 0,")
print("khien toan bo khoa don vao chung mot bucket duy nhat.")
print("Khi m la so nguyen to (nhu 17), no khong chia het cho cac uoc")
print("thuong gap trong du lieu thuc te (boi so cua 2, 4, 8, 16, ...),")
print("nen k mod m rai deu hon tren cac bucket, giam va cham dang ke.")
