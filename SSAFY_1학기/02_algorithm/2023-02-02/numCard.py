T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    card = list(map(int, list(input())))

    c_list = [0] * (max(card) + 1)

    for i in range(len(card)):
        c_list[card[i]] += 1

    for i in range(len(c_list) - 1, -1, -1):
        if c_list[i] == max(c_list):
            print(f"#{tc} {i} {c_list[i]}")
            break

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())  # 숫자 카드의 개수
#     numbers = input()  # 숫자 카드들이 주어지는데, 공백이 업시 붙여서 입력받는다.
#
#     # 숫자 카드 개수를 세줄 카운트 배열
#     counts = [0] * 10
#
#     # numbers 에 있는 숫자 하나씩 보면서 개수 세기
#     for num in numbers:
#         counts[int(num)] += 1  # num 카드의 등장 횟수 증가
#
#     # 카드의 최대 개수
#     max_count = 0
#     # 가장 큰 카드 수 (최대 개수가 같은게 여러개일 경우)
#     max_num = 0
#
#     # 카드 번호가 뒤로 갈수록 커진다는 점을 이용해서 부등호만 살짝 바꾸면 최대 번호까지 알수 있다.
#     for i in range(10):
#         if counts[i] >= max_count:
#             max_count = counts[i]
#             max_num = i
#
#     # for i in range(9, -1, -1):
#     #     if counts[i] > max_count:
#     #         max_count = counts[i]
#     #         max_num = i
#
#     print(f"#{tc} {max_num} {max_count}")