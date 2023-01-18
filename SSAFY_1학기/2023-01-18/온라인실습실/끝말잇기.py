words = ["round", "dream", "magnet", "tweet", "tweet", "trick", "kiwi"]

for idx in range(len(words)):

    # 탈락인 경우
    # 현재 idx 번째 문자열과 idx+1 번째 문자열을 비교
    # idx번째 문자열의 맨 끝 문자와
    # idx+1번째 문자열의 맨 앞문자를 비교 

    # 현재 idx 번째 문자열을 이전에 사용한 적이 있다면
    # 탈락
    print(words[idx], words[idx+1])
    if (words[idx][-1] != words[idx+1][0]) or (words[idx] in words[:idx]):
        print(f"{idx+1}번째 참가자가 탈락 하였습니다.")
        break
else:
    print("축하합니다. 아무도 탈락하지 않으셨습니다.")

# 다 맞는 경우는 에러 발생 ==> 인덱스 범위 벗어남
# 여러분이 해결해 보세요