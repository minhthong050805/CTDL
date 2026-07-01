def sap_xep_stack(stack):
    phu = []
    while stack:
        tmp = stack.pop()
        while phu and phu[-1] > tmp:
            stack.append(phu.pop())
        phu.append(tmp)
    while phu:
        stack.append(phu.pop())
    return stack


s = [3, 1, 4, 2, 5]
print(sap_xep_stack(s))

s2 = [3, 1, 2]
print(sap_xep_stack(s2))
