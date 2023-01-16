T = int(input())

for tc in range(1,T+1):
    t = int(input())

    scores = list(map(int , input().split()))

    score_cnt = [0] * 101

    max_score = 0
    for score in scores:
        # score 인덱스에 있는 값을 1 증가
        score_cnt[score] += 1

    # 최빈수 (몇번 나왔는지 구하기)
    max_score = max(score_cnt)

    # i 는 점수
    # 100 부터 시작해서 0까지 -1 씩 증가(감소)
    # for i in range(시작, 끝, 증가폭):

    for i in range(100, 0, -1):
        if score_cnt[i] == max_score:
            print(f"#{tc} {i}")
            break # 반복문 중간에 멈추고 종료
            
        

