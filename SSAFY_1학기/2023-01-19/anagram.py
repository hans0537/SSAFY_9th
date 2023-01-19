# A.    입력 예시 
words = ['eat','tea','tan','ate','nat','bat']

# 애너그램 그룹 딕셔너리로 묶기
anagrams = {}

# 애너그램 => 순서를 섞어서 다른 문자열 만들기
# 사전순으로 정렬해버리면?? 다 똑같아진다.
# 정렬한 다음에 비교해서 같으면 같은 애너그램 그룹에 속한다.

for word in words:
    # 단어를 사전순으로 정렬하기
    temp = sorted(word)
    # 정렬 결과가 리스트가 되어버리니까 다시 문자열로 만들기
    temp = "".join(temp)
    
    if anagrams.get(temp):
        # 정렬 결과가 이미 딕셔너리에 존재하는지 검사
        anagrams[temp].append(word)
    else:
        # 존재하지 않으면 새로운 리스트를 만들어서 추가
        anagrams[temp] = [word]

print(anagrams.values())