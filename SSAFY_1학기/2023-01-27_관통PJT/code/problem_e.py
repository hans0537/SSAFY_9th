import requests
from pprint import pprint


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
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
