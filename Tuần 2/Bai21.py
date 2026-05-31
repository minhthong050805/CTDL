a = [7, 2, 5, 10, 8]  # vidu
k = 2  # vidu

left, right = max(a), sum(a)
ans = right

while left <= right:
    mid = (left + right) // 2
    pieces = 1
    current_sum = 0
    for num in a:
        if current_sum + num > mid:
            pieces += 1
            current_sum = num
        else:
            current_sum += num

    if pieces <= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)