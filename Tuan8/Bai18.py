def polynomial_hash(s, p=31, m=10**9 + 9):
    h = 0
    p_pow = 1
    for c in s:
        h = (h + (ord(c) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return h


words = ["abc", "cba", "abd", "hello"]
p = 31
m = 10**9 + 9
for w in words:
    print(f"h('{w}') = {polynomial_hash(w, p, m)}")

print()
print(f"p = {p} (so nguyen to, lon hon bang chu cai su dung) giup phan biet")
print("thu tu ky tu, khac voi ham tong ma ASCII don gian (Bai 17).")
print(f"m = {m} (so nguyen to lon) giup gia tri hash phan bo deu va giam")
print("xac suat va cham do hieu ung sinh nhat (birthday paradox).")
