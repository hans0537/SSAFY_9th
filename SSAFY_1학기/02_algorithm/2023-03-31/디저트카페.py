dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

# 움직이는 순서
# 우하 => 좌하 => 좌상 => 우상
RD = 0  # 우하
LD = 1  # 좌하
LU = 2  # 좌상
RU = 3  # 우상


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


# visited : 방문체크
# dir : 현재 내 방향
# now : 좌표 정보
# now[0] = r, now[1] = c
def travel(visited, dir, now):
    global answer
    # 종료 조건
    # 도착한 경우 종료 (현재 위치 == 출발 위치)
    # 방향도 오른쪽 위를 보고 있어야 돌아온 것이다.
    if now == start and dir == RU:
        answer = max(answer, len(visited))
        return

    # 재귀 호출
    # 현재 방향으로 쭉 가거나 (dir + 0)
    # 다음 방향으로 바꿔서 가거나 (dir + 1)
    # 방향 바뀌는 순서가 우하, 좌하, 좌상, 우상 순서 고정
    for d in range(2):
        dir += d

        # 방향을 더이상 바꾸면 안될때
        if dir > 3:
            break

        # 다음 위치 계산
        nr = now[0] + dr[dir]
        nc = now[1] + dc[dir]

        # 다음 위치로 갈껀데, 다음위치가 범위 안
        # 전에 먹었던 디저트 종류도 아니어야 한다.
        if is_valid(nr, nc) and cafe_map[nr][nc] not in visited:
            # 디저트 먹고 다음 탐색
            visited.append(cafe_map[nr][nc])
            travel(visited, dir, (nr, nc))
            visited.pop()


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    cafe_map = [list(map(int, input().split())) for _ in range(n)]

    # 일단 갈 수 없다고 해놓고 진행
    answer = -1

    # 모든 위치에서 탐색 시작
    # 근데 방향은 오른쪽 아래로만 갈꺼야
    # 밑에서 출발하는 경우(위쪽 방향오는 경우 중복 체크 안해도 됨) 중복 방지
    for r in range(n):
        for c in range(n - 1):
            start = (r, c)
            # 방문체크, 방향, 내위치
            travel([], RD, (r, c))

    print(f"#{tc} {answer}")