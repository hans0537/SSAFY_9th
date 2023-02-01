for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    cnt = 0

    # 배열의 2번째 인덱스부터 건물임으로 2부터~ 배열길이 -2 전까지 탐색
    for i in range(2, len(building) - 2):
        # 현재 위치에서 앞뒤 2칸씩 배열을 내림차순으로 정렬후
        s = sorted(building[i-2:i+3], reverse=True)
        # 현재 위치 건물과 정렬한 배열의 0번째가 같으면 1번째의 차이를 카운트
        # 같지 않으면 현재위치 건물보다 큰 건물이 있으므로 조망권 확보 X
        if building[i] == s[0]:
            cnt += s[0] - s[1]

    print(f"#{tc} {cnt}")