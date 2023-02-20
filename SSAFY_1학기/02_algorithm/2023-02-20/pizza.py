def enqueue(item):
    global orear
    orear += 1
    ovenQ[orear] = item

def dequeue():
    global ofront
    ofront += 1
    return ovenQ[ofront]

def isEmpty():
    return orear == ofront

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    pizzaQ = list(map(int, input().split()))
    next_i = 0  # 피자를 꺼내올 피자의 번호

    ovenQ = [0] * 1000
    orear = ofront = -1

    # 오븐에 차례대로 피자를 넣기
    for i in range(N):
        enqueue((next_i, pizzaQ[next_i]))
        next_i += 1

    # 마지막에 꺼낸 피자의 번호
    ans = -1
    while True:
        tmp = dequeue()
        if tmp[1] // 2 != 0:
            enqueue((tmp[0], tmp[1] // 2))
        else:
            if next_i == M:
                if isEmpty():
                    ans = tmp[0]
                    break
            else:
                enqueue((next_i, pizzaQ[next_i]))
                next_i += 1

    print(f'#{tc} {ans + 1}')