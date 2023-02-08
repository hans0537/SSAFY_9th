def my_reverse(string):
    new_string = ''
    n = len(string)
    # 빈 문자열 만들고 뒤에서부터 이어 붙이는 방법
    # for i in range(n - 1, -1, -1):
    #     new_string += string[i]
    # return new_string

    # 앞뒤를 차례로 바꾸는 방법
    s2 = list(string)

    for i in range(n // 2):
        s2[i], s2[n - i - 1] = s2[n - i - 1], s2[i]

    print(s2)

def simple_strcmp(s1, s2):
    # s1과 s2의 아스키 코드 값을 비교해서
    # 사전 순서 리턴 (앞서면 음수, 나중이면 양수)
    return ord(s1) - ord(s2)

def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
    return i

def itoa(num):
    ret = ""
    # 숫자 하나씩 떼와서 (일의자리부터) 문자열로 바꾸기
    while num > 0:
        i = num % 10
        ret += chr(ord('0') + i)
        num //= 10

    return ret[::-1]

print(my_reverse('as1df'))
print(simple_strcmp('A', 'B'))
s = itoa(123)
print(s)
print(type(s))