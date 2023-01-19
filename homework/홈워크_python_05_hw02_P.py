# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    tmp = n
    while n > 0:
        tmp += n % 10
        n //= 10
    return tmp

print(fn_d(91))
print(fn_d(100))
print(fn_d(21))


gen_nums = []

def r_check(n):
    if n == 1:
        return
    gen_nums.append(fn_d(n))
    return r_check(n - 1)

def is_selfnumber(n):
    r_check(n)

    if n not in gen_nums:
        print(f'{n} : 셀프 넘버 입니다.')
    else:
        print(f'{n} : 셀프 넘버가 아닙니다.')

is_selfnumber(1000)