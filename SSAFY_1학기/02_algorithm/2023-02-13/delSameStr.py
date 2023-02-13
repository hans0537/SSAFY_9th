T = int(input())
for tc in range(1, T + 1):
    str = input()

    stack = []
    for i in str:
        if len(stack) == 0:
            stack.append(i)
        elif len(stack) != 0 and stack[len(stack) - 1] != i:
            stack.append(i)
        else:
            a = stack.pop()
            if i != a:
                stack.append(a)

    print(f'#{tc} {len(stack)}')

