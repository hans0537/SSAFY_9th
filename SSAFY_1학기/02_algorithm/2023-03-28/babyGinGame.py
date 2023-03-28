T = int(input())
def baby(lst):

    for i in lst:
        if i >= 3:
            return True

    for i in range(8):
        if lst[i] >= 1 and lst[i + 1] >= 1 and lst[i + 2] >= 1:
            return True

    return False

for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    
    for i in range(0, 12, 2):
        # 12개의 카드를 p1, p2 번갈아 선택
        p1[lst[i]] += 1
        p2[lst[i + 1]] += 1
        if i >= 4:  # 3개 뽑았을때부터 체크 시작
            # p1 부터
            if baby(p1):
                print('#{} 1'.format(tc))
                break
            # p2 부터
            elif baby(p2):
                print('#{} 2'.format(tc))
                break
    else:
        print('#{} 0'.format(tc))
