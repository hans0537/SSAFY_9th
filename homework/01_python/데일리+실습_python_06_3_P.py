def count_vowels(s):
    # 개수를 저장할 변수 선언
    cnt = 0
    # 모음 배열
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in s:
        # 대문자가 있을수 있으니 lower 로 비교
        if i.lower() in vowels:
            cnt += 1
    
    return cnt


print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3

