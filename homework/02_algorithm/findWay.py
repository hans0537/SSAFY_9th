for tc in range(1, 11):
    n, e = map(int, input().split())
    adj1 = [0] * 100
    adj2 = [0] * 100
    visited = [0] * 100
    stack = []
    lst = list(map(int, input().split()))
    turn = 1
    # 번갈아 가며 길 정보 넣기
    for i in range(0, e*2, 2):
        if turn == 2:
            adj2[lst[i]] = lst[i + 1]
            turn -= 1
        else:
            adj1[lst[i]] = lst[i + 1]
            turn += 1

    s = 0 # 시작 A 지점
    print(f'#{tc}', end=' ')
    while True:
        # 만약 B지점 도착시 
        if s == 99:
            print(1)
            break
        
        # 리스트에 해당하는 길이 있으면 이동
        for w in (adj1[s], adj2[s]):
            if visited[w] == 0:
                stack.append(w)
                s = w
                visited[w] = 1
                break
        # 없으면 되돌아가서 다른 길로 찾기
        else:
            if stack:
                s = stack.pop()
            else:
                print(0)
                break
