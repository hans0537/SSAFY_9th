T = int(input())

for tc in range(1, T + 1):
    money = int(input())

    m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8
    for i in range(len(m_list)):
        change[i] = money // m_list[i]
        money %= m_list[i]

    print(f'#{tc}')
    print(*change)

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())  # 거스름돈
#
#     money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#     # 화폐 종류 = 8가지
#     change = [0] * 8
#
#     # 화폐 종류 8가지에 대해서 거스름돈 걸러주기 반복
#     for i in range(8):
#         cnt = 0
#         # 남은 거스름돈 n 이 지금 화폐단위 money[i] 이상이라면 거스름돈으로 현재 화폐 사용 가능
#         # 현재 화폐 가치만큼 거스름돈 빼주고 사용 횟수 증가
#         while n >= money[i]:
#             n -= money[i]
#             cnt += 1
#         # i 번째 화폐의 사용 갯수를 적어준다.
#         change[i] = cnt
#
#     print(f"#{tc}")
#
#     ans = ""
#     for c in change:
#         ans += str(c) + " "
#     print(ans)
