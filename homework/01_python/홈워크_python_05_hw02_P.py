# # fn_d(91) 
# # 출력 예시 
# # 101

# 기본 방법
# def fn_d(n):
#     tmp = n
#     while n > 0:
#         tmp += n % 10
#         n //= 10
#     return tmp

# 짧은 코드 방법
def fn_d(n):
    return n + sum(map(int,list(str(n))))

# 입력예시
print(fn_d(91))
print(fn_d(100))

# 셀프 넘버 판별 함수
gen_nums = []
def is_selfnumber(n):
    for i in range(1,n + 1):
        gen_nums.append(fn_d(i))

    if n not in gen_nums:
        print(f'{n} : 셀프 넘버 입니다.')
    else:
        print(f'{n} : 셀프 넘버가 아닙니다.')

is_selfnumber(1)
is_selfnumber(3)
is_selfnumber(5)
is_selfnumber(7)
is_selfnumber(9)
is_selfnumber(10)
is_selfnumber(20)
is_selfnumber(31)

