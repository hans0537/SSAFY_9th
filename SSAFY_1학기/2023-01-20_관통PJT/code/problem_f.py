import json
import random

# 명대사 퀴즈 
def tagline_quiz(movies):
    # 명대사와 영화 제목의 정보를 저장한 딕셔너리 생성
    dic = {}

    for i in movies:
        # 각 영화의 id값.json 파일을 로드 
        movie = open('data/movies/'+ str(i.get('id')) + '.json', encoding='utf-8')
        movie_detail = json.load(movie)
        
        dic[movie_detail.get('tagline')] = i.get('title')

    return dic

# 평점대별 영화 리스트
def vote_movies(movies):
    # 평점대 별 영화 제목을 저장한 딕셔너리 
    dic = {}

    for i in movies:
        v = i.get('vote_average')

        if v in dic:
            dic[v].append(i.get('title'))
        else:
            dic[v] = [i.get('title')]

    return dic

# 가장 인기 있는 영화 1순위
def max_pop_movie(movies):
    max_pop = 0
    title = ''
    for i in movies:
        if i.get('popularity') > max_pop:
            max_pop = i.get('popularity')
            title = i.get('title')
    
    return title

# 연도별 영화 리스트 뽑기
def yearly_movies(movies):
    # 연도별 영화 저장할 딕셔너리 선언
    dic = {}
    
    for i in movies:
        year = i.get('release_date')[:4]
        if year in dic:
            dic[year].append(i.get('title'))
        else:
            dic[year] = [i.get('title')]

    return dic
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies = json.load(movies_json)

    while True:
        print("==========영화 정보 사이트==========")
        print("1. 영화 정보 보기\n2. 영화 명대사 맞추기\n0. 종료")

        sel1 = int(input("선택: "))

        if sel1 == 1:
            while True:
                print("====================================")
                print("1. 연도별 영화 보기\n2. 인기 1순위 영화 보기 \n3. 평점대별 영화 보기\n0. 뒤로가기")

                sel2 = int(input("선택: "))
                print("====================================")
                if sel2 == 1:
                    result = yearly_movies(movies)

                    for key, value in sorted(result.items()):
                        print(f"{key}년 : {value}")
                elif sel2 == 2:
                    result = max_pop_movie(movies)
                    print(f"1순위 영화 : {result}")
                elif sel2 == 3:
                    dic = vote_movies(movies)
                    
                    for i in dic.keys():
                        print(i)

                    vote = float(input("평점대를 입력해 주세요: "))
                    print("====================================")

                    if vote not in dic.keys():
                        print("해당 평점은 없습니다")
                    else:
                        print(f"{vote}점 영화 목록들 : \n{dic.get(vote)}")
                elif sel2 == 0:
                    break
                else:
                    print("번호를 잘못 입력했습니다.")
                
        elif sel1 == 2:
            print("====================================")
            print("5 문제중 3 문제를 맞추면 통과 입니다!!")
            quiz = tagline_quiz(movies)
            # 5번 체크 변수
            cnt = 0
            # 점수 변수
            score = 0
            # 중복 체크 리스트
            check = []
            while True:
                if cnt == 5:
                    break
                question, answer = random.choice(list(quiz.items()))
                
                if question in check or question == "":
                    continue
                
                print(f"[현재 스코어 : {cnt} | {score}]")
                check.append(question)
                print("====================================")
                print("문제 :", question)
                my_ans = input("정답: ")

                if answer.replace(" ", "") == my_ans.replace(" ", ""):
                    print("###정답!!!###")
                    cnt += 1
                    score += 1
                else:
                    print("###오답입니다!!! ###\n###정답은:", answer,"###")
                    cnt += 1
            print(f"[최종 스코어 : {cnt} | {score}]")        
            if score >= 3:
                print("###통과 하셨습니다!!!###")
            else:
                print("###탈락!! 다음에 다시 시도해보세요~###")
        elif sel1 == 0:
            break
        else:
            print("번호를 잘못 입력했습니다.")
