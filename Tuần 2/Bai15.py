a = [1, 2, 3, 4, 5]  # vidu
k = 4  # vidu
x = 3  # vidu

left, right = 0, len(a) - k

while left < right:
    mid = (left + right) // 2
    if x - a[mid] > a[mid + k] - x:
        left = mid + 1
    else:
        right = mid

ans = a[left : left + k]
print(ans)