lst = [1,2,3,4,5]
n = 5

# idx : idx번째 자리의 주인을 다른 누군가와 바꾸겠다.

def perm(idx):
    # 종료 조건
    if idx == n:
        print(lst)
        return

    # 재귀 호출
    # 현재 idx 번째 숫자와 자리를 바꿀 i 번째 숫자를 선택
    # idx == i 이면 자리를 바꾸지 않겠다는 의미
    for i in range(idx, n):
        # 자리 바꿔보고
        lst[idx], lst[i] = lst[i], lst[idx]
        perm(idx + 1)
        lst[idx], lst[i] = lst[i], lst[idx]


def perm2(cnt):
    # 종료 조건
    # 교환 횟수를 다 사용 했다면 최대 상금 구하기
    if cnt == N:

        return

    # 재귀 호출
    # 교환 횟수가 남았다면 카드 바꾸기
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용하기 때문에
    # 자리 위치 2개(i,j)를 교환 마다 새로 정해 주어야 한다.
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j], S[i]
            perm2(cnt + 1)
            S[i], S[j] = S[j], S[i]

S = [1,2,3,4,5]
N = 2
if N > len(S):
    N = len(S)
