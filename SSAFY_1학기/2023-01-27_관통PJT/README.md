# 02_pjt

## problem_a.py

```python
def popular_count():
    # 내 api key 
    api_key = 'a719d72e722ce5b82da9a04d59337764'
    
    # 요청할 url 주소
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'

    # 요청받은 JSON 데이터를 response에 저장
    response = requests.get(url).json().get('results')
    
    # 넘어온 데이터에서 'results'에 해당하는 리스트의 길이를 반환
    return len(response)
```

1. python install requests 명령어로 requests 모듈을 설치한다.
2. url 로 원하는값을 요청하고 받아온다.
3. 요청을 보낼시 고유한 api_key값이 필요하다.

## problem_b.py

```python
def vote_average_movies():
    # 내 api key 
    api_key = 'a719d72e722ce5b82da9a04d59337764'
    lang = 'ko-KR'
    
    # 요청할 url 주소
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language={lang}'

    # 요청받은 JSON 데이터를 response에 저장
    response = requests.get(url).json().get('results')
    
    result_list = []

    # 넘어온 json 데이터에서 평점비교후 배열에 저장
    for i in response:
      if i.get('vote_average') >= 8:
        result_list.append(i)
    
    return result_list
```

1. 넘어온 데이터의 특징과 타입을 꼼꼼히 파악하여 가공한다.

## problem_c.py

```python
def ranking():
  # 내 api key 
  api_key = 'a719d72e722ce5b82da9a04d59337764'

  # lang
  lang = 'ko-KR'
  
  # 요청할 url 주소
  url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language={lang}'

  # 요청받은 JSON 데이터에 'results'를 바로 가져와 response에 저장
  response = requests.get(url).json().get('results')

  # 배열에 저장되어있는 딕셔너리의 'vote_average'의 밸류로 정렬하여
  sort_list = sorted(response, key=(lambda x : x['vote_average']), reverse=True)

  # 상위 5개만 리스트로 반환
  return sort_list[:5]
```

1. lambda 익명함수를 활용하여 딕셔너리들을 저장한 리스트를 정렬한다.
2. key에는 정렬할 기준이 될 value를 지정한다.

## problem_d.py

```python
def recommendation(title):
    # 내 api key 
    api_key = 'a719d72e722ce5b82da9a04d59337764'
    
    # lang
    lang = 'ko-KR'

    # 요청할 url 주소
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language={lang}&query={title}'
    response = requests.get(search_url).json().get('results')
    
    #검색한 영화 정보가 없다면 None 반환후 종료
    if len(response) == 0:
        return None

    # 응답받은 결과중 첫번째 영화의 id값 저장
    search_id = response[0].get('id')

    # 받아온 id를 다시 api 요청
    recom_url = f'https://api.themoviedb.org/3/movie/{search_id}/recommendations?api_key={api_key}&language={lang}'
    response = requests.get(recom_url).json().get('results')
    
    # 요청 받은 데이터 (추천 영화)들의 제목들을 리스트에 저장후 반환
    r_list = []
    for i in response:
        r_list.append(i.get('title'))
    
    return r_list
```

1. 빈데이터가 넘어올때 예외 처리가 필요하다
2. 데이터의 특징을 잘 파악하여 원하는 데이터를 가져올때 다른 곳으로 또 요청을 해야 할때가 있다.

## problem_e.py

```python
def credits(title):
    # 내 api key 
    api_key = 'a719d72e722ce5b82da9a04d59337764'
    
    # lang
    lang = 'ko-KR'

    # 요청할 url 주소
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language={lang}&query={title}'

    # 넘어온 데이터가 없을때 인덱싱을 할수 없으므로 예외처리로 None을 리턴후 종료 
    try:
        # 데이터가 있을시 첫번째 영화의 id를 가져온다
        search_id = requests.get(search_url).json().get('results')[0].get('id')
    except:
        return None

    # 출연진 데이터를 받을 url
    credit_url = f'https://api.themoviedb.org/3/movie/{search_id}/credits?api_key={api_key}&language={lang}'
    response = requests.get(credit_url).json()

    cast = []
    directing = []
    
    # 넘어온 데이터의 각각 해당하는 키값에 밸류를 요구사항과 비교하여 각 리스트에 저장
    for i in response.get('cast'):
        if i.get('cast_id') < 10:
            cast.append(i.get('name'))

    for i in response.get('crew'):
        if i.get('department') == 'Directing':
            directing.append(i.get('name'))

    # 딕셔너리 형태의 자료로 저장후 반환
    result = {
        'cast' : cast,
        'directing' : directing
    }

    return result
```

1. try/except 문을 활용하여 넘어온 데이터가 비었을때 index 에러발생시 없는 데이터라고 예외처리를 활용한다.

## problem_f.py

```python
# 영화진흥위원회 api key
api_key = '9acf67875889f8c9a1f614d0d3457e85'

# 박스오피스
def boxOffice(date, sel):
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={api_key}&targetDt={date}&weekGb={sel-1}'

    response = requests.get(url).json()

    # 넘어온 데이터가 오류 코드이면 해당 메세지 리턴
    if 'faultInfo' in response:
        return response.get('faultInfo').get('message')[:26]

    # 박스 오피스 정보
    response = response.get('boxOfficeResult')
    
    # 리턴 해줄 문자열 설정
    res = response.get('boxofficeType') + ' [' + response.get('showRange') + ']\n'
    
    m_list = response.get('weeklyBoxOfficeList')

    for i in m_list:
        res += f"순위: {i.get('rank')} | 제목: {i.get('movieNm')}\n"
        res += f"[개봉일자: {i.get('openDt')} | 누적 관객수 : {i.get('audiAcc')} | 누적 매출액: {i.get('salesAcc')}]\n\n"

    return res

# 영화 검색
def searchMovie(movie):
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={api_key}&movieNm={movie}'

    # 해당 영화에 대한 정보가 없을시 예외 처리
    try:
        movie_cd = requests.get(url).json().get('movieListResult').get('movieList')[0].get('movieCd')
    except:
        return '해당 영화에 대한 정보가 없습니다.'

    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={api_key}&movieCd={movie_cd}'

    movie_detail = requests.get(url).json().get('movieInfoResult').get('movieInfo')

    res = f"[제목 : {movie_detail.get('movieNm')}]\n"
    res += f"개봉일: {movie_detail.get('openDt')}\n"
    res += f"상영 시간: {movie_detail.get('showTm')}\n장르: "
    for i in movie_detail.get('genres'):
        res += f"{i.get('genreNm')}, "
    
    # 감독은 한명만 출력
    res += f"\n감독: {movie_detail.get('directors')[0].get('peopleNm')}\n배우: "
    
    # 배우는 3명 까지만 출력
    for i in movie_detail.get('actors')[:3]:
        res += f"{i.get('peopleNm')}, "

    res += f"\n관람가: {movie_detail.get('audits')[0].get('watchGradeNm')}"
    return res

# 배우 검색
def searchActor(actor):
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={api_key}&peopleNm={actor}'

    # 해당 영화에 대한 정보가 없을시 예외 처리
    try:
        actor_detail = requests.get(url).json().get('peopleListResult').get('peopleList')[0]
    except:
        return '해당 배우에 대한 정보가 없습니다.'

    res = f"[이름 : {actor_detail.get('peopleNm')}]\n"
    res += f"직업: {actor_detail.get('repRoleNm')}\n"
    res += f"참여 작품: {actor_detail.get('filmoNames')}"

    return res

if __name__ == '__main__':

    while True:
        print('===== 영화 정보 조회 프로그램 =====')
        print('1. 박스오피스 조회\n2. 영화 검색\n3. 배우 검색\n0. 종료')

        sel1 = int(input('선택: '))

        if sel1 == 1:
            while True:
                print('=========================================')
                date = input('조회할 날짜 입력하세요(형식: yyyymmdd): ')

                print('1. 주간 (월~일)\n2. 주말(금~일)\n3. 주중(월~목)')
                sel2 = int(input('선택: '))

                if 1 <= sel2 <= 3:
                    print('=========================================')
                    print(boxOffice(date, sel2))
                    break
                else:
                    print('번호를 잘못 입력했습니다.')
        elif sel1 == 2:
            print('=========================================')
            movie = input('영화 검색: ')
            print(searchMovie(movie))
        elif sel1 == 3:
            print('=========================================')
            actor = input('배우 검색: ')
            print(searchActor(actor))
        elif sel1 == 0:
            print('프로그램 종료')
            break
        else:
            print('번호를 잘못 선택했습니다')
```

1. 박스오피스, 감독, 배우를 검색하는 프로그램을 구현
2. 해당 api의 데이터 타입, 필요한 데이터를 꼼꼼히 체크하여 요청을 해야한다.