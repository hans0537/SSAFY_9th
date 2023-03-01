dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

def func():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    cnt = 0
                    for k in range(N):
                        mx = i + dx[d] * k
                        my = j + dy[d] * k

                        if 0 <= mx < N and 0 <= my < N:
                            if arr[mx][my] == 'o':
                                cnt += 1
                            else:
                                if cnt == 5:
                                    break
                                else:
                                    cnt = 0

                    if cnt == 5:
                        return True
    return False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    if func():
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))

