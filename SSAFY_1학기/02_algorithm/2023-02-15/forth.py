T = int(input())
for tc in range(1, T + 1):
    s = input().split()
    stack = []
    ans = 0
    for i in s:
        if '0' <= i <= '9':
            stack.append(int(i))
        else:
            if i == '.' and len(stack) == 1:
                ans = stack.pop()
            else:
                if len(stack) < 2:
                    break
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    stack.append(op1 + op2)
                elif i == '-':
                    stack.append(op1 - op2)
                elif i == '*':
                    stack.append(op1 * op2)
                elif i == '/':
                    stack.append(op1 // op2)
    print(f'#{tc} error') if ans == 0 else print(f'#{tc} {ans}')
