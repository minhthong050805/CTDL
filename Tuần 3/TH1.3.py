def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

# Ví dụ sử dụng
arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
print("Mảng chưa được sắp xếp là:", arr)
bubbleSort(arr)
print("Mảng được sắp xếp là:", arr)

# Nhận xét:
# Input: một mảng gồm n phần tử (có thể là số nguyên hoặc số thực).
# Output: mảng đã được sắp xếp theo thứ tự tăng dần.
# Ví dụ: Input [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
#        Output [-50, -10, -2, 3, 6, 7, 14, 17, 25, 100]
# Độ phức tạp: Best case O(n), Average/Worst case O(n^2).
