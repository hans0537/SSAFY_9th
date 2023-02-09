# 최대 공약수 GCD : GREATEST COMMON DIVISOR

# 최소 공배수 LCM : LEAST COMMON MULTIPLE

# a > b
def gcd(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def new_gcd(a, b):
    # a % b == 0
    # return b
    # else
    # gcd(b, a % b)

    if b == 0:
        return a
    else:
        return new_gcd(b, a % b)

def lcm(a, b):
    return a * b // new_gcd(a, b)

a = 20
b = 15
print(gcd(a,b))
print(new_gcd(a,b))
print(lcm(a,b))
