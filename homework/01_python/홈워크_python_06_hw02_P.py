# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

def group_anagrams(arr):
    dic = {}
    for i in arr:
        # 같은 알파벳 조합의 단어를 sort 하면 같으므로
        # 딕셔너리의 키값으로 주고 밸류에 기존 단어를 하나씩 넣는다.
        if ''.join(sorted(i)) not in dic:
            dic[''.join(sorted(i))] = [i]
        else:
            dic.get(''.join(sorted(i))).append(i)

    return list(dic.values())

# 사용자 입력 버전
words = list(map(str, input("공백을 기준으로 단어 입력: ").split()))
print(group_anagrams(words))


# print("# 입력 예시 1) ['eat','tea','tan','ate','nat','bat']")
# print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
# print()
# print("# 입력 예시 2) ['let','tel','polo','cake','rat','art','pool','loop']")
# print(group_anagrams(['let','tel','polo','cake','rat','art','pool','loop']))

