# 데코레이터

# def ko_hello(name):
#     print(f'안녕하세요, {name}님!')

# def en_hello(name):
#     print(f'Hello, {name}!')

# def add_emoji(name, func):
#     func(name)
#     print('^~^//')

# ko_hello('aiden')
# en_hello('aiden')

# add_emoji('aiden', ko_hello)
# add_emoji('aiden', en_hello)

def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print("^~^//")

    return wrapper

def tears_decorator(func):
    def wrapper(name):
        print("ㅠ.ㅠ//")
        func(name)

    return wrapper

# new_func = emoji_decorator(ko_hello)
# new_func('aiden')

# emoji_decorator(ko_hello)('aiden')
# emoji_decorator(en_hello)('aiden')

# 위와 같은 호출을 데코레이터를 활용하면
@tears_decorator
@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')

ko_hello('aiden')