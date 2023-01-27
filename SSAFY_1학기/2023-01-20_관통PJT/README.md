# 01_pjt

## problem_a.py

```python
def movie_info(movie):
    dic = {}
    dic['id'] = movie.get('id')
    dic['title'] = movie.get('title')
    dic['poster_path'] = movie.get('poster_path')
    dic['vote_average'] = movie.get('vote_average')
    dic['overview'] = movie.get('overview')
    dic['genre_ids'] = movie.get('genre_ids')
    
    return dic

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    pprint(movie_info(movie_dict))
```

1. main 에서 json 파일이 저장되어 있는 경로를 통해 파일을 불러온다.
2. utf-8 인코딩을 안하면 한글이 깨질 수 도 있다.
3. pprint는 데이터를 보기 좋게 출력하는 하나의 모듈.
4. 파일에 있는 데이터들을 파이썬 딕셔너리에 추가를 할 수 있는 부분은 편리한것 같다.


## problem_b.py

```python
def movie_info(movie, genres):
    dic = {}
    dic['id'] = movie.get('id')
    dic['title'] = movie.get('title')
    dic['poster_path'] = movie.get('poster_path')
    dic['vote_average'] = movie.get('vote_average')
    dic['overview'] = movie.get('overview')
    dic['genre_ids'] = movie.get('genre_ids')

    # 장르 이름 리스트 생성
    gen_names = []
    for i in dic.get('genre_ids'):
        for j in genres:
            if j.get('id') == i:
                gen_names.append(j.get('name'))
    
    # genre_ids 의 밸류를 장르 이름 리스트로 변경
    dic['genre_ids'] = gen_names
    # dic 딕셔너리 안에 genre_ids => genre_names로 키명 변경
    dic['genre_names'] = dic.pop('genre_ids')
    
    return dic

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

1. problem a처럼 정보들을 넣은후 요구사항에서 장르 id들을 장르 name과 바꾼다.
2. 해당 영화의 장르 id들 마다 genre 파일의 id 와 대조하여 장르를 가져온 리스트를 생성.
3. 그이후 기존 키값의 이름을 genre_names로 바꾸고 밸류에다가 장르 리스트를 교체 하였다.
4. 외부파일(json 파일)을 받아와 원하는데로 가공하고 데이터를 조작할 수 있다는 것은 외부에서 json 파일을 불러와 다양하게 가공을 할수 있을것 같다.

## problem_c.py

```python
import json
from pprint import pprint

def movie_info(movies, genres):
    infoList = []
    
    for i in movies:
        dic = {}
        dic['id'] = i.get('id')
        dic['title'] = i.get('title')
        dic['poster_path'] = i.get('poster_path')
        dic['vote_average'] = i.get('vote_average')
        dic['overview'] = i.get('overview')
        dic['genre_ids'] = i.get('genre_ids')

        # 장르 이름 리스트 생성
        gen_names = []
        for i in dic.get('genre_ids'):
            for j in genres:
                if j.get('id') == i:
                    gen_names.append(j.get('name'))
        
        # genre_ids 의 밸류를 장르 이름 리스트로 변경
        dic['genre_ids'] = gen_names
        # dic 딕셔너리 안에 genre_ids => genre_names로 키명 변경
        dic['genre_names'] = dic.pop('genre_ids')

        infoList.append(dic)
        
    return infoList
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

```
1. b와 비슷하지만 하나의 영화 정보가 아닌 다수의 영화 정보를 한번에 처리 하는 방법을 생각 해내는게 관건이라고 생각했다.


## problem_d.py

```python
import json

def max_revenue(movies):

    # 키를 영화 제목, 밸류를 revenue 저장할 딕셔너리 생성
    dic = {}
    
    for i in movies:
        
        # 각 영화의 id값.json 파일을 로드 
        movie = open('data/movies/'+ str(i.get('id')) + '.json', encoding='utf-8')
        movie_detail = json.load(movie)
        
        # 각 영화의 상세 파일에서 reveneue 값을 딕셔너리에 저장
        dic[i.get('title')] = movie_detail.get('revenue')

    # 딕셔너리 value 최대값의 키를 리턴
    return max(dic, key=dic.get)
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```
1. 영화 마다의 세부 정보 파일을 불러오는 방법으로 한번더 open()을 걸어 주었다.
2. 가장 간단하게 많은 데이터를 다룰 수 있는방법을 생각해 보았다.
3. key를 영화 제목으로 설정후 요구사항에서 수입의 중복값은 없다고 했으니 value를 수입으로 설정하였다.
4. 그후 밸류를 기준으로 최대값의 key즉 영화 제목을 출력 하였다. 


## problem_e.py

```python
import json

def dec_movies(movies):
    # 12 월 영화 리스트 선언
    dec_list = []
    
    for i in movies:
        
        # 각 영화의 id값.json 파일을 로드 
        movie = open('data/movies/'+ str(i.get('id')) + '.json', encoding='utf-8')
        movie_detail = json.load(movie)
        
        # 날짜 문자열 슬라이싱
        if movie_detail.get('release_date')[5:7] == '12':
            dec_list.append(movie_detail.get('title'))

    return dec_list
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

```

1. d와 같이 다량의 데이터 에서 필요한것만 추출하여 문자열 슬라이싱을 활용하여 필요한 값만 가져와 저장하였다.
2. 요구사항에 따라 사용해야 하는 자료를 선택하는것이 고민이었다.


## problem_f.py (선택 과제)

```python
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

```

1. a~e를 연습해본 결과 주어진 데이터로 다양한 시도를 해볼 수 있다는 생각을 하여 4가지 정도의 메소드를 선언하여 영화 정보 사이트 프로그램을 코딩 했다.
2. 원하는 데이터를 끌어오기 위해 복잡한 자료 속을 정리하면서 가져오는 과정을 통해 자료에 대한 이해도가 높아졌다.
3. 차후 json 파일의 데이터들을 다루려면 해당 파일에 대한 데이터 가이드 표를 잘 봐야 한다고 생각한다. 어떤 데이터가 무엇을 의미 하는지 확실하게 알아야 명확한 데이터 관리, 가공, 조작을 할 수 있을것 같다. 

