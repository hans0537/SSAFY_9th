dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def dfs(x, y, p):

# 가로 검색
def rowCheck(x, p):
    tmp = board[x]
    if p in tmp[x+1:]:
        j = board[x].index(p)
    if p in tmp[:x]:
        j = board[x].index(p)




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    board[N//2 - 1][N//2 - 1] = 2
    board[N//2 - 1][N//2] = 1
    board[N//2][N//2 - 1] = 1
    board[N//2][N//2] = 2

    for i in range(M):
        y, x, p = map(int, input().split())
        # dfs(x-1, y-1, p)