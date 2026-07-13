def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    best_seq = []
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            current = num
            while current + 1 in num_set:
                current += 1
                length += 1
            if length > best:
                best = length
                best_seq = list(range(num, current + 1))
    return best, best_seq


A = [100, 4, 200, 1, 3, 2]
length, seq = longest_consecutive(A)
print(f"Mang: {A}")
print(f"Do dai day lien tiep dai nhat: {length}")
print(f"Day tim duoc: {seq}")
