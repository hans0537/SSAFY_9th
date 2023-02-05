T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    cnt = 0
    i = 0
    while i + k < n:

        for j in range(k, 0, -1):
            if i + j in charge:
                i += j
                cnt += 1
                break
        else:
            cnt = 0
            break
    print(cnt)

# def drive(K, N):
#     # 버스를 운행하는 함수
#     # return == 0 : 충전소가 제대로 배치되어있지 않아서 완주 불가능
#     # return > 0 : 충전소가 제대로 배치되어 있다. => 충전 횟수를 리턴
#
#     last = 0  # 버스가 마지막으로 충전했던 위치
#     next = K  # 버스가 최대로 이동한 위치 (초기값은 한번 이동한 상태로)
#     count = 0  # 충전한 횟수
#
#     # 버스가 종점에 도착할때까지 계속 반복
#     while next < N:
#
#         # 버스가 이동한 위치에 충전기가 있나 없나 검사
#         while stop[next] == 0:
#             # 충전기가 없다면 뒤로 한칸씩 돌아가면서 충전기를 찾을때까지 뒤로 이동
#             next -= 1
#             if next == last:
#                 # 만약 뒤로 계속 가다가 내가 마지막으로 충전했던 위치까지 와버렸다면
#                 # 다시 앞으로 가봤자 다시 돌아올테니까 충전소가 제대로 설치되어있지 않다는 것이다!!
#                 # return 0 => 운행 불가!
#                 return 0
#
#         # 충전기가 제대로 설치되어 있다면
#         # 마지막 충전 위치를 갱신
#         last = next
#         # 다음 위치로 이동
#         next += K
#         # 충전 횟수 1 증가
#         count += 1
#
#     # 다음 위치로 이동했는데 이동한 거리가 N 보다 크다면 완주 했다는 거니까 반복을 종료
#     return count
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     # K : 이동할수 있는 거리
#     # N : 버스가 가야할 거리
#     # M : 충전기 개수
#
#     charge = list(map(int, input().split()))  # 충전소 정보
#     stop = [0] * N  # 정류장 리스트 (1: 충전소가 있는 정류장 / 0 : 충전소가 없는 정류장)
#     for x in charge:  # x는 충전소가 있는 정류장 위치
#         stop[x] = 1  # x위치엔 충전소가 있다고 표시
#     answer = drive(K, N)
#     print(f"#{tc} {answer}")

