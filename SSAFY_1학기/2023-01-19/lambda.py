# def my_magic_func(n):
#     return n * 10

# map_obj = map(my_magic_func, [1, 2, 3])
# rlt = list(map_obj)

map_obj = map(lambda x : x * 10, [1, 2, 3])
rlt = list(map_obj)

print(rlt)

# 소괄호를 이용하여 이름 없는 함수 정의
rlt = (lambda x : x * x)(4)
print(rlt)

my_func = lambda n : n * 2
my_func(2)

# 위와 같은 의미
def pow(x):
    return x * x


v = (lambda x: x*x)(4)
print(v)

# 나중에 또 사용하려면 변수에 람다함수 지정
my_lambda = lambda x: x*x

print(my_lambda(4))

# sorted(key, reverse)
# key => 정렬 기준 (함수)

# 딕셔너리를 정렬
# 딕셔너리는 비시퀀스형이라서 순서가 의미가 없다.
# 순서가 없는데 정렬을 어떻게 할까?
# 시퀀스가 있는 형태로 바꿔서 정렬을 한다.
# items()

score = {"홍경환" : 2, "이정현" : 1, "김재만" : 3}
print(score.items())

# x 는 정렬할 아이템중 하나
# x[0] 은 키, x[1] 는 밸류
print(sorted(score.items(), key=lambda x:x[1]))

def key_f(x):
    return x[1]

print(sorted(score.items(), key=key_f))