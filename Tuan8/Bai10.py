def first_unique_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


s = "leetcode"
result = first_unique_char(s)
print(f"Chuoi: '{s}'")
print(f"Ky tu khong lap dau tien: '{result}'")
