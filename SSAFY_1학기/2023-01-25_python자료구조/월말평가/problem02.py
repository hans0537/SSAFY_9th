# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    # 최소값을 구할때 변수의 초기값은 적당히 큰 값
    min_val = 99999
    # 최대값을 구할때 변수의 초기값은 적당히 작은 값
    max_val = 0

    for score in scores:
        # 최소값 구하기
        if min_val > score:
            min_val = score
        
        # 최대값 구하기
        if max_val < score:
            max_val = score

    return min_val, max_val


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
