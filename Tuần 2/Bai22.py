a = [1, 3]  # vidu
b = [2]  # vidu

if len(a) > len(b):
    a, b = b, a

x_len, y_len = len(a), len(b)
left, right = 0, x_len

while left <= right:
    partition_x = (left + right) // 2
    partition_y = (x_len + y_len + 1) // 2 - partition_x

    max_left_x = float("-inf") if partition_x == 0 else a[partition_x - 1]
    min_right_x = float("inf") if partition_x == x_len else a[partition_x]

    max_left_y = float("-inf") if partition_y == 0 else b[partition_y - 1]
    min_right_y = float("inf") if partition_y == y_len else b[partition_y]

    if max_left_x <= min_right_y and max_left_y <= min_right_x:
        if (x_len + y_len) % 2 == 1:
            ans = float(max(max_left_x, max_left_y))
        else:
            ans = (
                max(max_left_x, max_left_y) + min(min_right_x, min_right_y)
            ) / 2.0
        break
    elif max_left_x > min_right_y:
        right = partition_x - 1
    else:
        left = partition_x + 1

print(ans)