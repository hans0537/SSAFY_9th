T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    cnt = 1
    ans = 1
    for i in range(n - 1):
        if lst[i] < lst[i + 1]:
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 1
    print(f'#{tc} {ans}')