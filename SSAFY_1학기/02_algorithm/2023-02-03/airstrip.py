T = int(input())
# 활주로 체크 함수
def check(land, x):
    global cnt
    # 평평한 길이를 저장하는 변수
    tmp = 1
    for i in range(len(land) - 1):
        # 만약 같은 높이면 tmp 증가
        if land[i] == land[i + 1]:
            tmp += 1
        # 올라가는 길이고 tmp가 활주로 길이보다 크면 설치후 초기화
        elif land[i] - land[i + 1] == -1 and tmp >= x:
            tmp = 1
        # 내려가는 길이고 이전에 활주로 가 겹치지 않으면 활주로 설치했다고 가정
        elif land[i] - land[i + 1] == 1 and tmp >= 0:
            tmp = -x + 1
        # 활주로 유효성이 다 안되면 함수 종료
        else:
            return
    
    # 마지막으로 tmp 가 음수이면 내려온 길이 있다 말아서 tmp가 0보다 크면 cnt 증가
    if tmp >= 0:
        cnt += 1

for tc in range(1, T + 1):
    n, x = map(int, input().split())
    cnt = 0
    land = [0]*n

    for i in range(n):
        land[i] = list(map(int, input().split()))
        # 가로 입력 받을 때 바로 check 함수 돌리기
        check(land[i], x)

    # 세로 체크
    for i in range(n):
        tmpLst = []
        for j in range(n):
            tmpLst.append(land[j][i])
        check(tmpLst, x)

    print(f'#{tc} {cnt}')
