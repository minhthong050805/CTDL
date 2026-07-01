def dao_nguoc_chuoi(s):
    stack = []
    for c in s:
        stack.append(c)
    result = []
    while stack:
        result.append(stack.pop())
    return ''.join(result)


def dao_nguoc_mang(arr):
    stack = []
    for x in arr:
        stack.append(x)
    result = []
    while stack:
        result.append(stack.pop())
    return result


print(dao_nguoc_chuoi("abc"))
print(dao_nguoc_mang([1, 2, 3, 4, 5]))
