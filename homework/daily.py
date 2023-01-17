str_lst = input('문자열을 입력하세요. : ')

#문자열을 소문자화 후 배열에 각 단어 저장
str_lst = str_lst.lower().split(" ")

#현재 단어와 다음 단어의 각 뒤와 앞 알파벳 비교
for i in range(len(str_lst) - 1):
    if(str_lst[i][-1] != str_lst[i + 1][0]):
        print('Fail')
        break
else:
    print('Pass')