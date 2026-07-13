def row_window_hashes(matrix, q, base=256, mod=10**9 + 7):
    m = len(matrix)
    n = len(matrix[0])
    result = []
    high_order = pow(base, q - 1, mod)
    for r in range(m):
        row = matrix[r]
        hashes = [0] * (n - q + 1)
        h = 0
        for j in range(q):
            h = (h * base + row[j]) % mod
        hashes[0] = h
        for j in range(1, n - q + 1):
            h = (h - row[j - 1] * high_order) % mod
            h = (h * base + row[j + q - 1]) % mod
            h %= mod
            hashes[j] = h
        result.append(hashes)
    return result


def find_submatrix(big, small):
    m, n = len(big), len(big[0])
    p, q = len(small), len(small[0])
    if p > m or q > n:
        return []

    base = 256
    mod = 10**9 + 7

    big_row_hashes = row_window_hashes(big, q, base, mod)
    col_count = n - q + 1
    row_count = m - p + 1

    target_row_hashes = []
    for r in range(p):
        hr = 0
        for x in small[r]:
            hr = (hr * base + x) % mod
        target_row_hashes.append(hr)

    target_hash = 0
    for hr in target_row_hashes:
        target_hash = (target_hash * base + hr) % mod

    high_order_col = pow(base, p - 1, mod)
    matches = []

    for j in range(col_count):
        column = [big_row_hashes[r][j] for r in range(m)]

        window_hash = 0
        for r in range(p):
            window_hash = (window_hash * base + column[r]) % mod

        for i in range(row_count):
            if window_hash == target_hash:
                if all(big[i + dr][j:j + q] == small[dr] for dr in range(p)):
                    matches.append((i, j))
            if i < row_count - 1:
                window_hash = (window_hash - column[i] * high_order_col) % mod
                window_hash = (window_hash * base + column[i + p]) % mod
                window_hash %= mod

    return matches


big_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [9, 6, 7, 1],
]
small_matrix = [
    [6, 7],
    [2, 3],
]

result = find_submatrix(big_matrix, small_matrix)
print("Ma tran lon:")
for row in big_matrix:
    print(f"  {row}")
print("Ma tran con can tim:")
for row in small_matrix:
    print(f"  {row}")
print(f"Cac vi tri (hang, cot) tim thay (chi so goc trai tren): {result}")
