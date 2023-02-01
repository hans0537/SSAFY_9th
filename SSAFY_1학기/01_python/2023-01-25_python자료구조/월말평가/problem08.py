# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    
    result = ""

    for char in word:
        if char.isupper():
            char = chr(65 + (ord(char) - 65 + n) % 26)
        elif char.islower():
            char = chr(97 + (ord(char) - 97 + n) % 26)
        result += char

    return result

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
