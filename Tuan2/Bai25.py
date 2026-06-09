x = [1, 2, 3, 4, 7]  # vidu
m = 3  # vidu

x.sort()
left, right = 1, x[-1] - x[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    last_position = x[0]
    for i in range(1, len(x)):
        if x[i] - last_position >= mid:
            count += 1
            last_position = x[i]

    if count >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)