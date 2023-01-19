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

def is_selfnumber(n):
    