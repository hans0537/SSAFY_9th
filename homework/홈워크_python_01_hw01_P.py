score = {
    'python': 80,
    'django': 89,
    'web': 83
}   

#algorithm 점수 추가 (90점)
score['algorithm'] = 90

#python 점수 80 -> 85  수정
score['python'] = 85

#전체 점수 평균 구하기
print(sum(score.values()) / len(score))