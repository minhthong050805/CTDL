def hash_set_order_independent(s):
    result = 0
    for item in s:
        result ^= hash(item) & 0xFFFFFFFFFFFFFFFF
    return result


def hash_multiset_order_independent(s):
    total = 0
    for item in s:
        total = (total + hash(item)) & 0xFFFFFFFFFFFFFFFF
    return total


s1 = {1, 2, 3}
s2 = {3, 1, 2}
s3 = [1, 2, 3]
s4 = [3, 2, 1]

print(f"hash_set({{1,2,3}}) = {hash_set_order_independent(s1)}")
print(f"hash_set({{3,1,2}}) = {hash_set_order_independent(s2)}")
print(f"Bang nhau? {hash_set_order_independent(s1) == hash_set_order_independent(s2)}")

print()
print(f"hash_multiset([1,2,3]) = {hash_multiset_order_independent(s3)}")
print(f"hash_multiset([3,2,1]) = {hash_multiset_order_independent(s4)}")
print(f"Bang nhau? {hash_multiset_order_independent(s3) == hash_multiset_order_independent(s4)}")

s5 = [1, 1, 2]
s6 = [1, 2, 2]
print()
print(f"hash_multiset([1,1,2]) = {hash_multiset_order_independent(s5)}")
print(f"hash_multiset([1,2,2]) = {hash_multiset_order_independent(s6)}")
print(f"Bang nhau (dung phai khac vi so lan xuat hien khac nhau)? "
      f"{hash_multiset_order_independent(s5) == hash_multiset_order_independent(s6)}")
