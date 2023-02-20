for tc in range(1, 11):
    input()
    numbers = [0] + list(map(int, input().split()))

    # 원형 큐 사용
    rear = 8
    front = 0
    check = True
    while check:
        for i in range(1, 6):
            rear = (rear + 1) % 9
            front = (front + 1) % 9
            if numbers[front] - i <= 0:
                numbers[rear] = 0
                check = False
                break
            numbers[rear] = numbers[front] - i

    if front > rear:
        print(f'#{tc}', *(numbers[front + 1:] + numbers[:rear + 1]))
    else:
        print(f'#{tc}', *numbers[front + 1: rear + 1])


    '''
    # 선형 큐 사용
    rear = 7
    front = -1
    check = True
    while check:
        for i in range(1, 6):
            rear += 1
            front += 1
            if numbers[front] - i <= 0:
                numbers[rear] = 0
                check = False
                break
            numbers[rear] = numbers[front] - i
    '''