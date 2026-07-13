def rabin_karp_search(text, pattern, base=256, mod=10**9 + 7):
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    positions = []
    high_order = pow(base, m - 1, mod)

    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                positions.append(i)
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * high_order) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            window_hash %= mod

    return positions


text = "zabcd"
pattern = "abc"
positions = rabin_karp_search(text, pattern)
print(f"Van ban: '{text}'")
print(f"Mau can tim: '{pattern}'")
print(f"Vi tri xuat hien: {positions}")

text2 = "abababcabababcab"
pattern2 = "abc"
positions2 = rabin_karp_search(text2, pattern2)
print()
print(f"Van ban: '{text2}'")
print(f"Mau can tim: '{pattern2}'")
print(f"Vi tri xuat hien: {positions2}")
