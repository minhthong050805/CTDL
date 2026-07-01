def kiem_tra_ngoac(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0


print(kiem_tra_ngoac("([]{})"))
print(kiem_tra_ngoac("([)]"))
print(kiem_tra_ngoac("{[()]}"))
print(kiem_tra_ngoac("((()"))
