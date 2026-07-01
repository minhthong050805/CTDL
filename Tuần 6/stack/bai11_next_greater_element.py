def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result


print(next_greater_element([2, 1, 3]))
print(next_greater_element([4, 5, 2, 25]))
print(next_greater_element([13, 7, 6, 12]))
