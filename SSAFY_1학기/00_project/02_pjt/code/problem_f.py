import requests
from pprint import pprint

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