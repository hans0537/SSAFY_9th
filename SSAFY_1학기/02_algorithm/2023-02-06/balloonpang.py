T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m


for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # 풍선 정보
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = 0

    # 모든 위치에대해서 풍선 다 터뜨려 보고
    # 그중에 최대값 구하기
    for r in range(n):
        for c in range(m):
            # 현재 꽃가루 수 + 상하좌우 꽃가루 수
            cnt = arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 다음 위치가 배열의 범위를 벗어나지 않는지 꼭 검사
                if is_valid(nr, nc):
                    cnt += arr[nr][nc]

            if max_cnt < cnt:
                max_cnt = cnt

    print(f"#{tc} {max_cnt}")
