T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = sorted(list(map(int, input().split())))

    mi = 1e9
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if lst[i] != lst[i + 1] and lst[j] != lst[j + 1]:
                A = i + 1
                B = j - i
                C = N - j - 1

                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    mi = min(max(A, B, C) - min(A, B, C), mi)
    if mi == 1e9:
        mi = -1
   
    print('#{} {}'.format(tc, mi))
