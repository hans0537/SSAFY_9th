# Advance
# 원자의 정보를 담을 클래스 선언
class atom:
    def __init__(self, x, y, d, k):
        self.x = x
        self.y = y
        self.d = d
        self.k = k

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 원자 인스턴스들의 배열
    atom_list = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atom_list.append(atom(x, y, d, k))

    energy = 0
    #    상  하  좌  우   => 0.5초 에 만나는 경우도 있으니...
    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]

    # 원자가 하나 남으면 종료
    while len(atom_list) > 1:
        # 각 원자의 이동방향을 0.5초 이동시키기
        for i in range(len(atom_list)):
            atom_list[i].x += dx[atom_list[i].d]
            atom_list[i].y += dy[atom_list[i].d]

        dic = {}
        # 동일 좌표에 있는 원자들을 저장할 딕셔너리
        for i in atom_list:
            a = (i.x, i.y)
            if dic.get(a):
                dic[a].append(i)
            else:
                dic[a] = [i]

        # 원자들을 다시 넣을 배열 초기화
        atom_list = []
        for v in dic.values():
            # 동일한 좌표에 있는 원자들이면 (2개 이상)
            if len(v) >= 2:
                # 에너지 생산
                for a in v:
                    energy += a.k
            # 넘어가지 않은 좌표들 한에서 다시 배열에 넣기
            else:
                if -1000 <= v[0].x <= 1000 and -1000 <= v[0].y <= 1000:
                    atom_list.append(v[0])

    print(f'#{tc} {energy}')
#
# T = int(input())
# for tc in range(1, 1+T):
#     n = int(input())
#     atom = [list(map(int, input().split())) for _ in range(n)]
#     # 격자 중간에서 만날 수도 있기 때문에 0.5초 단위로 이동한다고 가정했음
#     d = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
#
#     result = 0
#
#     # 아톰 개수가 2개 이하가 되면 만날 아톰이 없으니까 종료
#     while len(atom) >= 2:
#         # 모든 아톰을 0.5초 단위로 이동시킨다
#         for i in range(len(atom)):
#             atom[i][0] = atom[i][0] + d[atom[i][2]][0]
#             atom[i][1] = atom[i][1] + d[atom[i][2]][1]
#
#         # 좌표를 딕셔너리로 표현
#         location = {}
#         # 각 아톰들을 순회하면서 좌표: [아톰들]의 형태로 넣어준다.
#         for a in atom:
#             try:
#                 location[(a[0], a[1])].append(a)
#             except Exception:
#                 location[(a[0], a[1])] = [a]
#
#         # 아톰 리스트를 초기화하고
#         atom = []
#         for l in location:
#
#             if len(location[l]) >= 2:
#                 # 만약 같은 위치에 아톰이 여러개라면 결과값에 아톰의 에너지들을 결과값에 넣어주고
#                 for at in location[l]:
#                     result += at[3]
#             else:
#                 # 위치에 아톰이 1개라면 범위내에 있는 아톰들은 아톰 리스트에 다시 넣어준다.
#                 if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000:
#                     atom.append(location[l][0])
#
#     print(f'#{tc}', result)