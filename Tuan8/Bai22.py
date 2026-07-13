def hash_combine(*values):
    C = 0x9e3779b97f4a7c15
    result = 0
    for v in values:
        h = hash(v)
        result ^= (h + C + (result << 6) + (result >> 2)) & 0xFFFFFFFFFFFFFFFF
        result &= 0xFFFFFFFFFFFFFFFF
    return result


def hash_pair(a, b):
    return hash_combine(a, b)


pairs = [(1, 2), (2, 1), (1, 2), (3, 4), (0, 0)]
for a, b in pairs:
    print(f"hash_pair({a}, {b}) = {hash_pair(a, b)}")

print()
print(f"hash_pair(1,2) == hash_pair(2,1)? "
      f"{hash_pair(1, 2) == hash_pair(2, 1)}")
print("Nhan xet: hash_combine ket hop hash cua tung thanh phan bang cach")
print("dich bit va XOR, giup phan biet thu tu (a,b) khac (b,a), va giam")
print("va cham so voi cach cong hash don gian.")
