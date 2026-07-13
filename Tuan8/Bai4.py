def common_elements(a, b):
    set_a = set(a)
    set_b = set(b)
    return set_a & set_b


A = [1, 2, 3]
B = [2, 3, 4]
result = common_elements(A, B)
print(f"Mang A: {A}")
print(f"Mang B: {B}")
print(f"Phan tu chung: {result}")
