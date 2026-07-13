def hash_sum_chars(s, m):
    total = sum(ord(c) for c in s)
    return total % m


m = 97
words = ["abc", "cba", "bca", "hello", "world"]
for w in words:
    print(f"h('{w}') = {hash_sum_chars(w, m)}")

print()
print(f"'abc' va 'cba' co cung hash: {hash_sum_chars('abc', m) == hash_sum_chars('cba', m)}")
print("Nhuoc diem: ham bam nay chi phu thuoc tong ma ky tu, nen moi hoan vi")
print("(anagram) cua cung mot tap ky tu deu cho ra cung mot gia tri bam,")
print("gay va cham rat nhieu voi cac chuoi la hoan vi cua nhau.")
