import requests
from pprint import pprint


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

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
