def h_mod(k, m):
    return k % m


keys = [7, 17, 27, 37, 47, 100, 233]
m = 10

print(f"Hop bang m = {m}")
distribution = {i: [] for i in range(m)}
for k in keys:
    idx = h_mod(k, m)
    distribution[idx].append(k)
    print(f"h({k}) = {k} mod {m} = {idx}")

print()
print("Phan bo vao cac bucket:")
for i in range(m):
    print(f"  bucket {i}: {distribution[i]}")
