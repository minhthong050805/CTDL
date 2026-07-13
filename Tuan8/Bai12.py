def subarray_sum_equals_k(a, k):
    prefix_count = {0: 1}
    prefix_sum = 0
    count = 0
    for num in a:
        prefix_sum += num
        need = prefix_sum - k
        if need in prefix_count:
            count += prefix_count[need]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    return count


A = [1, 1, 1]
k = 2
result = subarray_sum_equals_k(A, k)
print(f"Mang: {A}, k = {k}")
print(f"So doan con co tong bang k: {result}")
