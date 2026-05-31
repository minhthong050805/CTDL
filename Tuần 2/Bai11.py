a = [3, 4, 5, 1, 2]  # vidu

left, right = 0, len(a) - 1

while left < right:
    mid = (left + right) // 2
    if a[mid] > a[right]:
        left = mid + 1
    else:
        right = mid

print(a[left])