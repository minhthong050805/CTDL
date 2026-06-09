matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]  # vidu
k = 8  # vidu

n = len(matrix)
left, right = matrix[0][0], matrix[n - 1][n - 1]
ans = left

while left <= right:
    mid = (left + right) // 2
    count = 0
    col = n - 1
    for row in range(n):
        while col >= 0 and matrix[row][col] > mid:
            col -= 1
        count += col + 1

    if count >= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)