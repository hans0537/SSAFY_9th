T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # 컨테이너
    w = list(map(int, input().split()))
    # 트럭
    t = list(map(int, input().split()))

    # greedy ?? 큰 컨테이너 부터 옮기자 ==> 큰 트럭부터 선택

    # 내림차순 정렬하면 첫번째 원소가 가장 큰게 된다. => 0부터 시작 가능
    w.sort(reverse=True)
    t.sort(reverse=True)

    # 다음에 이동할 컨테이너, 트럭의 인덱스
    wi = 0
    ti = 0

    # 옮긴 화물의 총 중량
    moved = 0
    
    # 트럭을 보낼수 있을때 까지
    while wi < n and ti < m:
        # 현재 옮길 차례의 화물이 트럭에 실을수 있다면 총 중량 증가
        if w[wi] <= t[ti]:
            moved += w[wi]
            wi += 1
            ti += 1
        # 트럭이 작아서 wi 번째 화물을 못 옮길 경우
        else:
            wi += 1

    print(f"#{tc} {moved}")
