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
    dx = [-0.5, 0.5, 0, 0]
    dy = [0, 0, -0.5, 0.5]

    # 원자가 하나 남으면 종료
    while len(atom_list) > 1:
        # 각 원자의 이동방향을 0.5초 이동시키기
        for i in range(len(atom_list)):
            atom_list[i].x += dx[atom_list[i].d]
            atom_list[i].y += dy[atom_list[i].d]

        dic = {}
        # 동일 좌표에 있는 원자들을 저장할 딕셔너리
        for i in range(len(atom_list)):
            a = (atom_list[i].x, atom_list[i].y)
            if dic.get(a) is None:
                dic[a] = [atom_list[i]]
            else:
                dic[a].append(atom_list[i])

        atom_list = []
        for v in dic.values():
            print(v[0].x, v[0].y, v[0].d, v[0].k)
            if len(v) >= 2:
                for a in v:
                    energy += a.k
            else:
                if -1000 <= v[0].x <= 1000 and -1000 <= v[0].y <= 1000:
                    atom_list.append(v[0])

    print(f'#{tc} {energy}')