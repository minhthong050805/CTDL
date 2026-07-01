def tinh_rpn(bieu_thuc):
    stack = []
    tokens = bieu_thuc.split()
    ops = {'+', '-', '*', '/'}
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            stack.append(float(token))
    return stack[0]


print(tinh_rpn("3 4 + 2 *"))
print(tinh_rpn("5 1 2 + 4 * + 3 -"))
