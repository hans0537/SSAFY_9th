T = int(input())

def solve(arr):
    for lst in arr:     # 행을 체크
        if len(set(lst)) != 9:
            return 0

    # 전치 행렬
    arr_t = list(zip(*arr)) # 세로 체크
    for lst in arr_t:
        if len(set(lst)) != 9:
            return 0
    # for i in range(len(arr)):
    #     tmp = []
    #     for j in range(len(arr)):
    #         tmp.append(sudo[j][i])
    #         if len(set(tmp)) != 9:
    #             return 0

    for i in (0,3,6):
        for j in (0,3,6):       # 3*3 격자
            lst = arr[i][j : j+3] + arr[i + 1][j : j + 3] + arr[i + 2][j : j + 3]
            if len(set(lst)) != 9:
                return 0
    return 1


for tc in range(1, T + 1):
    sudo = [list(map(int, input().split())) for _ in range(9)]
    ans = solve(sudo)
    print(f'#{tc} {ans}')

