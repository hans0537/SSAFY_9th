def collatz(num):
    cnt = 0

    while num > 1:
        if cnt > 500:
            return -1
    
        # 짝수일경우
        if num % 2:
            num = num * 3 + 1
            cnt += 1
        # 홀수일 경우
        else:
            num = num // 2
            cnt += 1
            
    return cnt

print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1
