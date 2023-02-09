def bm_search(txt, pat):
    # txt 인덱스
    ti = 0
    # pat 인덱스
    pi = 0

    n = len(txt)  # 텍스트의 길이
    m = len(pat)  # 패턴의 길이

    skip = {}

    # 패턴 안에 있는 문자는 몇 칸 건너 뛸지 정해준다.
    for p in pat:
        skip[p] = m - 1 - pat.rfind(p)

    # 만약 딕셔너리에 없는 경우는 패턴에 없다는 뜻이니까 그냥 패턴의 길이만큼
    # 건너뛴다.

    print(skip)

    # 패턴의 제일 뒤 글자부터 비교
    ti = m - 1
    while ti < n:
        pi = m - 1  # 패턴의 뒤에서부터 비교 시작

        # 같은 문자가 나오면 계속 앞으로 이동
        # 다른 문자가 나오면 건너뛰기 표를 참고해서 skip
        while txt[ti] == pat[pi]:
            if pi == 0:
                # 패턴의 맨 앞까지 와버리면 뒤에 있는 글자가 모두 같았다.
                # 기준 위치인 ti를 리턴
                return ti
            ti -= 1
            pi -= 1

        # 건너뛰기 표에 있는 문자가 나오면 표에 적힌대로 skip
        # 건너뛰기 표에 없는 문자가 나오면 패턴의 길이만큼 skip

        offset = skip.get(txt[ti]) if skip.get(txt[ti]) else m

        # 다시 비교를 시작할 위치를 정해준다.
        # 위에서 계산한 건너뛰기 만큼 이동
        ti += offset if offset > m - pi else m - pi

    # 여기까지 오면 (반복이 종료되면) 패턴 못찾음
    return -1


t = "zzzabcdabcdabcefabcd"
p = "abcdabcef"
print(f"res :", bm_search(t, p), t.find(p))
