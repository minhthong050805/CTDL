def group_by_first_letter(words):
    groups = {}
    for w in words:
        key = w[0]
        groups.setdefault(key, []).append(w)
    return groups


words = ["apple", "ant", "banana", "bear", "cat", "car", "dog"]
result = group_by_first_letter(words)
print(f"Danh sach tu: {words}")
print("Nhom theo chu cai dau:")
for k in sorted(result):
    print(f"  {k}: {result[k]}")
