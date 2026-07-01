A = [7, 3, 9, 12, 5, 8, 1]
x = 5
ket_qua = -1
for i in range(len(A)):
    so_sanh = (A[i] == x)
    print(f"i={i}, A[i]={A[i]}, A[i]==x? {so_sanh}")
    if so_sanh:
        ket_qua = i
        break
print("Vi tri tra ve:", ket_qua)
