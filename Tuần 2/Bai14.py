matrix = [[1, 3, 5], [7, 9, 11]]  # vidu
x = 9  # vidu

m = len(matrix)
n = len(matrix[0])
left, right = 0, m * n - 1
ans = False

while left <= right:
    mid = (left + right) // 2
    row = mid // n
    col = mid % n
    if matrix[row][col] == x:
        ans = True
        break
    elif matrix[row][col] < x:
        left = mid + 1
    else:
        right = mid - 1

print(ans)