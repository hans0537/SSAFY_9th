import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 상자 탑의 수
    n = int(input())
    # 최대값 => 초기값 정할떄 적당히 작은 값
    # 최소값 => 적당히 큰값
    maxV = 0

    # 상자 탑 높이 정보
    box = list(map(int, input().split()))
    cnt = []

    # 반복문을 돌면서 현재 위치의 높이에서 제일 위에 있는 상자의 낙차중에 가장 큰값을 구하면 된다.
    for i in range(n):
        # 현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물(상자)이 없다고 했을때 최대 낙차 구하기
        c = 0
        for j in range(i + 1, n):
            if box[i] > box[j]:
                c += 1
        cnt.append(c)

    for v in cnt:
        if maxV < v:
            maxV = v

    print(f"#{tc} {maxV}")
