words = ["round", "dream", "magnet", "tweet", "tweet", "trick", "kiwi"]

idx = 0

while idx < len(words) - 1:
    idx += 1
    if (words[idx-1][-1] != words[idx][0]) or (words[idx] in words[:idx]):
        print(f"{idx+1}번째 참가자 탈락")
        break
    if idx == len(words) - 1:
        print("축하합니다. 아무도 탈락하지 않으셨습니다.")
