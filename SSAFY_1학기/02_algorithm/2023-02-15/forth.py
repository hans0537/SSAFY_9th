T = int(input())
for tc in range(1, T + 1):
    s = input().split()
    stack = []
    ans = 0
    for i in s:
        if i.isdigit():
            stack.append(int(i))
        else:
            if i == '.':
                ans = stack.pop()
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    stack.append(op1 + op2)
                elif i == '-':
                    stack.append(op1 - op2)
                elif i == '*':
                    stack.append(op1 * op2)
                elif i == '/':
                    stack.append(op1 / op2)
