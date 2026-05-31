a = [1, 1, 2, 3, 3, 4, 4]  # vidu

left, right = 0, len(a) - 1

while left < right:
    mid = (left + right) // 2
    if mid % 2 == 1:
        mid -= 1
    if a[mid] == a[mid + 1]:
        left = mid + 2
    else:
        right = mid

print(a[left])