import requests


def popular_count():
    # 내 api key 
    api_key = 'a719d72e722ce5b82da9a04d59337764'
    
    # 요청할 url 주소
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'

    # 요청받은 JSON 데이터를 response에 저장
    response = requests.get(url).json().get('results')
    
    # 넘어온 데이터에서 'results'에 해당하는 리스트의 길이를 반환
    return len(response)

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
