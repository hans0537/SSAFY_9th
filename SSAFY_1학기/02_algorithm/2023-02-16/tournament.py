def winner(left, right):
    if (lst[left] == 1 and lst[right] == 3) or (lst[left] == 2 and lst[right] == 1) or (
            lst[left] == 3 and lst[right] == 2):
        return left
    elif (lst[left] == 3 and lst[right] == 1) or (lst[left] == 1 and lst[right] == 2) or (
            lst[left] == 2 and lst[right] == 3):
        return right
    else:
        if left < right:
            return left
        else:
            return right


def tournament(i, j):
    # 1. 종료 조건
    if i == j:
        return i

    # 2. 재귀 호출
    left = tournament(i, (i + j) // 2)
    right = tournament((i + j) // 2 + 1, j)
    return winner(left, right)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc} {tournament(0, n - 1) + 1}')
