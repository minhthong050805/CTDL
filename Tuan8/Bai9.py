def two_sum(a, target):
    seen = {}
    for i, num in enumerate(a):
        need = target - num
        if need in seen:
            return (seen[need], i)
        seen[num] = i
    return None


A = [2, 7, 11]
target = 9
result = two_sum(A, target)
print(f"Mang: {A}, target = {target}")
print(f"Ket qua (chi so): {result}")
