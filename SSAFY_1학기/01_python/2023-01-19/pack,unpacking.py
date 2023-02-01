# 패킹 / 언패킹 => *

# x, y = 1, 2
# z = 1, 2, 3

# 패킹
a, *b = 1, 2, 3, 4
print(a,b)

# 언패킹
def my_sum(a, b, c):
    return a + b + c

num_list = [10, 20, 30]

# rlt = my_sum(num_list[0], num_list[1], num_list[2])
rlt = my_sum(*num_list)

def my_sum(*values):
    rlt = 0
    for value in values:
        rlt += value

my_sum()        #0
my_sum(1,2,3)   #6

def test(**kwargs):
    print(kwargs, type(kwargs))
    return kwargs

test(name='asdf', age = 21)

# 나머지들은 자기들 끼리 패킹, 키워드는 키워드끼리 패킹(딕셔너리 형태)
def test(*args, **kwargs):
    print(kwargs, type(kwargs))
    return kwargs
test(1,2,3,4,name='asdf', age = 21)
