# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    x, y = position
    x += dx[M]
    y += dy[M]

    if 0 <= x < N and 0 <= y < N:
        return True
    
    return False



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == "__main__":
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
