T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    s_list = []
    for i in range(N):
        s_list.append(input())

    res = []
    # 가로 검색
    for i in range(N):
        for j in range(N - M + 1):
            if s_list[i][j:M + 1 + j] == s_list[i][j:M + 1 + j][::-1]:
                res.append(s_list[i][j:M + 1 + j])

    # 세로 검색
    for i in range(N):
        for j in range(N - M + 1):
            tmp = ''
            for k in range(M):
                tmp += s_list[j + k][i]
            if tmp == tmp[::-1]:
                res.append(tmp)

    print(f'#{tc} {"".join(res)}')

