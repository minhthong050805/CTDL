def mo_phong(lenh):
    stack = []
    for cmd in lenh:
        if cmd[0] == "push":
            stack.append(cmd[1])
        elif cmd[0] == "pop":
            if stack:
                print(f"pop -> {stack.pop()}")
            else:
                print("pop -> underflow")
    print(f"Trang thai cuoi: {stack}")


lenh = [("push", 5), ("push", 7), ("pop",), ("push", 3), ("pop",)]
mo_phong(lenh)
