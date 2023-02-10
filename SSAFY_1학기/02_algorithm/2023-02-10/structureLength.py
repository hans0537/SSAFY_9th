T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    maxV = 0
    for _ in range(N):
        # str으로 받아준다
        tmp = ''.join(input().split())
        arr.append(tmp)
        # 가로 건물 검색
        # 가로는 인풋 받을때 배열로 받았기에 조인을 한후
        # 0으로 스플릿하여 1만 있는 스트링 배열로 만들어준다
        # tmp 리스트를 map을 활용하여 각 len으로 해준 배열을 만들어준다
        # 즉 1이 연속된 길이가 모여진 리스트
        # max를 사용하여 기존 maxV와 비교를한다
        maxV = max(max(list(map(len, tmp.split('0')))), maxV)

    # 세로 건물 검색 (가로와 비슷한 방법)
    for i in range(M):
        tmp = ''
        for j in range(N):
            tmp += arr[j][i]
        tmp = tmp.split('0')
        maxV = max(max(list(map(len, tmp))), maxV)

    print(f'#{tc} {maxV}')