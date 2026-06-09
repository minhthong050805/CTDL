def bubble_Sort(arr):
    n = len(arr) 
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Ví dụ sử dụng
arr = [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]
bubble_Sort(arr)
print("Mảng được sắp xếp là:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

# Nhận xét:
# Input: một mảng gồm n phần tử (có thể là số nguyên hoặc số thực).
# Output: mảng đã được sắp xếp theo thứ tự tăng dần.
# Ví dụ: Input [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]
#        Output [-155, -30, -10, -1, 12, 15, 32, 52, 60, 71, 75, 90]
# Độ phức tạp: Best case O(n), Average/Worst case O(n^2).
