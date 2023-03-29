T = int(input())
def dfs(idx, money):
    global ans

    if ans <= money:
        return

    if idx >= len(plan):
        ans = min(ans, money)
        return

    # 0일일때 선택 X
    if plan[idx] == 0:
        dfs(idx + 1, money)

    # 1일 선택
    dfs(idx + 1, money + plan[idx] * price[0])

    # 1달 선택
    dfs(idx + 1, money + price[1])

    # 3달 선택
    dfs(idx + 3, money + price[2])

for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = 9999999999999
    dfs(0, 0)

    # 1년치는 따로 계산
    ans = min(ans, price[3])

    print('#{} {}'.format(tc, ans))