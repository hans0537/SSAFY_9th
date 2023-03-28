N = 10
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            print(i, j, k)


lst = [1,2,3,4,5]
N = 5
R = 3
# N개 중에 R개를 고르는 경우의 수

# 1. idx 번째 숫자를 고를지 않고를지 결정
def comb(idx, r, selected):
    # 종료 조건
    if idx == N:
        if r == R:
            print(selected)
        return

    # 재귀 호출
    # 고르고 진행
    selected.append(lst[idx])
    comb(idx + 1, r + 1, selected)
    # 고르지 않고 진행
    selected.pop()
    comb(idx + 1, r, selected)

# 2. R개 고를때까지 계속 선택
# 내가 idx번째 원소를 골랐다면, idx 이전에 있는 친구는 고려하지 않고
# 뒤에 있는것만 선택

def comb2(idx, selected):
    # 종료 조건
    if len(selected) == R:
        return
    
    # 재귀 호출
    # 현재 위치 idx 기준 i >= idx i 번째 숫자를 하나 고르고 진행
    for i in range(idx, N):
        comb2(i + 1, selected + [lst[i]])
    
comb(0, 0, [])