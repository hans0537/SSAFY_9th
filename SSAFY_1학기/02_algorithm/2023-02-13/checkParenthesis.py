T = int(input())
for tc in range(1, T + 1):
    str = input()

    stack = []
    ans = 1
    for i in str:
        if i == '(' or i == '{':
            stack.append(i)

        if i == ')' or i == '}':
            if len(stack) == 0:
                ans = 0
                break

            a = stack.pop()
            if (i == ')' and a != '(') or (i == '}' and a != '{'):
                ans = 0
                break

    if len(stack) > 0:
        ans = 0

    print(f'#{tc} {ans}')