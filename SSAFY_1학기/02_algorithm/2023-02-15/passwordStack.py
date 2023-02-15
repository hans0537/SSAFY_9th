for tc in range(1, 11):
    s = input().split()
    n = int(s[0])
    pw = s[1]

    stack = []
    for i in range(n):
        if len(stack) != 0 and stack[-1] == pw[i]:
            stack.pop()
            continue
        stack.append(pw[i])

    print(f'#{tc}', ''.join(stack))