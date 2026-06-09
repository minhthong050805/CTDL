def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
arr = [120, 35, 60, 42, 280, 7, 15, 19]
bubble_sort(arr)
print("Mảng sau khi sắp xếp:", arr)

# Nhận xét:
# Input: một mảng gồm n phần tử (có thể là số nguyên hoặc số thực).
# Output: mảng đã được sắp xếp theo thứ tự tăng dần.
# Ví dụ: Input [120, 35, 60, 42, 280, 7, 15, 19]
#        Output [7, 15, 19, 35, 42, 60, 120, 280]
# Độ phức tạp: Best case O(n), Average/Worst case O(n^2).
