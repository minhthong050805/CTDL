def duyet_va_dem(stack):
    phu = []
    print(f"So phan tu: {len(stack)}")
    print("Theo thu tu LIFO:", end=" ")
    while stack:
        val = stack.pop()
        print(val, end=" ")
        phu.append(val)
    print()
    while phu:
        stack.append(phu.pop())
    print(f"Stack sau khi khoi phuc: {stack}")


stack = [1, 2, 3]
duyet_va_dem(stack)
