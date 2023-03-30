T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(cnt, s, x, y):
    global ans

    if cnt == 7:
        lst.add(s)
        return
    
    # 4방향 탐색
    for d in range(4):
        mx = x + dx[d]
        my = y + dy[d]
        
        if 0 <= mx < 4 and 0 <= my < 4:
            dfs(cnt + 1, s + arr[x][y], mx, my)

for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    ans = 0
    lst = set()
    for i in range(4):
        for j in range(4):
            dfs(0, '', i, j)

    print('#{} {}'.format(tc, len(lst)))