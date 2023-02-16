def isValid(i):
    for k in range(i):
        # 만약 i의 값과 k의 값이 같으면 같은 세로에 있음
        if check[i] == check[k]:
            return 0
    return 1

def min_sum(i, s):
    global min_v
    global cnt
    cnt += 1
    if s > min_v:
        return
    if i == N:
        min_v = min(min_v, s)
        return

    for j in range(N):
        check[i] = j

        if isValid(i):
            min_sum(i + 1, s + board[i][j])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 인덱스와 값으로 같은 세로에 있는지 판별 가능
    check = [0] * N
    min_v = 1e9
    cnt = 0
    min_sum(0, 0)
    print(f'#{tc} {min_v}')
    print(cnt)